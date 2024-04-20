from django import forms
from django.contrib.auth.models import User
from reminder.models import Task

class Register(forms.ModelForm):
    class Meta:
        model   =   User
        # fields=   '__all__'
        fields  =   ["username","password","first_name","last_name","email"]

class Signin(forms.Form):
    username    =   forms.CharField()
    password    =   forms.CharField()

class Taskform(forms.ModelForm):
    class Meta:
        model   =   Task
        fields  =   ['name','deadline']
        # fields  =   ["name","due_date","due_time"]
        widgets =   {
            'deadline': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }