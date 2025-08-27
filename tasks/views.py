from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, "home.html")

#sesion para crear usuario
def signup(request):
    #cuando entramos a la pagina
    if request.method == "GET":
        #renderizamos el html
        return render(request, "signup.html", {
        "form" : UserCreationForm()
        })
    #y si enviamos los datos    
    else:
        #comparamos si ambas contraseñas son iguales
        if request.POST["password1"] == request.POST["password2"]:
            try:
                    #registramos usuarios
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                #guardamos dentro de la base de datos
                user.save()
                #iniciamos sesion
                login(request, user)
                #retornamos el render pero con un error
                return redirect(tasks)
            #si sale el error IntegrityError (el usuario ya existe)
            except IntegrityError:
                return render(request, "signup.html", {
                    "form" : UserCreationForm(),
                    "error" : "User alredy exists"
                    })
                
        return render(request, "signup.html", {
                    "form" : UserCreationForm(),
                    "error" : "Password do not match"
                    })
        
@login_required       
def tasks(request):
    #buscamos las tareas con el mismo usuario que el request
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull = True) #Esto devuelve las listas no completadas
    return render(request,"tasks.html", {
        "tasks" : tasks
    }) 

@login_required       
def tasks_completed(request):
    #buscamos las tareas con el mismo usuario que el request
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull = False).order_by('-datecompleted') #Esto devuelve las listas completadas en orden
    return render(request,"tasks.html", {
        "tasks" : tasks
    }) 

@login_required       
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {
            "form" : TaskForm()
        })
    else:
        try:
            #vuelve a crear un formulario con lo enviado en el POST para poder guardarlo
            form = TaskForm(request.POST)
            #en new_task guardamos los datos
            new_task = form.save(commit=False)
            #guardamos el usuario el cual creo el task
            new_task.user = request.user
            #guardamos enla base de datos
            new_task.save()
            return redirect("tasks")
        except ValueError: 
            return render(request, "create_task.html", {
            "form" : TaskForm(),
            "error" : "Please provide valid data"
        })

@login_required       
def task_detail(request, task_id):
    if request.method == "GET":
        #busca el objeto con esa primaryKey y si no lo encuentra tira error pero no cae el servidor
        task = get_object_or_404(Task, pk = task_id, user=request.user)
        #creamos un formulario con las instancias de task ya escritas
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {"task" : task, "form" : form})
    else:
        try:
            task = get_object_or_404(Task, pk = task_id, user=request.user)
            #creamos un formulario con las instancias enviadas en el POST
            form = TaskForm(request.POST, instance = task)
            #lo guardamos
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(request, "task_detail.html", {"task" : task, "form" : form,
                          "error" : "Error updating task"})

@login_required                   
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id, user = request.user)
    if request.method == "POST":
        task.datecompleted = timezone.now()
        task.save()
        return redirect("tasks")

@login_required           
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id, user = request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
            
        
        

#funcion para cerrar sesion
@login_required        
def signout(request):
    logout(request)
    return redirect("home")

#funcion para iniciar sesion
def signin(request):
    #si recien entramos a la pagina:
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form' : AuthenticationForm()
        })
    else:
        #guardamos el usuario ingresado
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        #si no lo encontro
        if user == None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm(),
                'error' : 'Username or password is incorrect'
            })
        #si lo encontro
        else:
            login(request, user)
            return redirect("tasks")