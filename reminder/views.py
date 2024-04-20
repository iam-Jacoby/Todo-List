from django.shortcuts import render,redirect
from django.views.generic import View
from reminder.forms import Register,Signin,Taskform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from reminder.models import Task
from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):                                         ########  -------  DECORATOR OF CHECKING IF WE ARE LOGGED - IN OR NOT  -------  
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id      =   kwargs.get("pk")
        obj     =   Task.objects.get(id=id)
        if obj.user !=  request.user:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form    =   Register()
        return render(request,"reg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form    =   Register(request.POST)
        if form.is_valid():
            form.save
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Added Successfully!")
        form    =   Register()
        return render(request,"reg.html",{"form":form})
    
class SignView(View):
    def get(self,request,*args,**kwargs):
        form    =   Signin()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form    =   Signin(request.POST)
        if form.is_valid():
            u_name  =   form.cleaned_data.get("username")
            pwd     =   form.cleaned_data.get("password")
            userobj =   authenticate(request,username=u_name,password=pwd)
            print(userobj)
            
            if userobj:
                print("Valid Cridentials")
                login(request,userobj)
                return redirect("index")
            
            else:
                print("Invalid Cridentials")

        return render(request,"login.html",{"form":form})
    
@method_decorator(signin_required, name="dispatch")
class TaskView(View):
    def get(self,request,*args,**kwargs):
        form    =   Taskform()
        data    =   Task.objects.filter(user=request.user).order_by('complete')
        return render(request,"index.html",{"form":form, "data":data})

    def post(self,request,*args,**kwargs):
        form    =   Taskform(request.POST)
        
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        
        else:
            print("Get Out")
        
        form    =   Taskform()
        data    =   Task.objects.filter(user=request.user)
        return render(request,"index.html",{"form":form, "data":data})

class TaskUpdate(View):
    def get(self,request,*args,**kwargs):
        id  =   kwargs.get("pk")
        # Task.objects.filter(id=id).update(complete=True)
        # messages.success(request,"Task Completed Successfully!")                      NEED THESE MESSAGES TO APPEAR
        qs  =   Task.objects.get(id=id)
        if qs.complete == True:
            qs.complete = False
            qs.save()
        elif qs.complete == False:
            qs.complete = True
            qs.save()

        return redirect("index")

@method_decorator(mylogin, name="dispatch")
class TaskDelete(View):
    def get(self,request,*args,**kwargs):
        id  =   kwargs.get("pk")
        Task.objects.filter(id=id).delete()
        return redirect("index")

@method_decorator(signin_required, name="dispatch")
class TaskEdit(View):
    def get(self,request,*args,**kwargs):
        id  =   kwargs.get("pk")
        qs  =   Task.objects.get(id=id)
        form    =   Taskform(instance=qs)
        return render(request,"edit.html",{"form":form})
    
    def post(self,request,**kwargs):
        id = kwargs.get("pk")
        qs = Task.objects.get(id=id)
        form=Taskform(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee Updated Successfully.")

        else:
            messages.error(request,"Failed to Update Employee.")
            print("Get Out")
        return redirect('index')



class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
    
class user_del(View):
    def get(self,request,*args,**kwargs):
        id  =   kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect("reg")