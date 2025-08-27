from django import forms
from .models import Task

class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        #hacemos que title sea un textinput y lo modificamos con boostrap con attrs
        widgets = {
            "title" : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : "Write a title"}),
            "description" : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Write a description'}),
            "important" : forms.CheckboxInput(attrs={'class': 'form-check-input, m-auto '}),
        } 