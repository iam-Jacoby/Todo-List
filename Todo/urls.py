"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from reminder.views import RegisterView,SignView,Signout,TaskView,TaskUpdate,TaskDelete,TaskEdit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',RegisterView.as_view(),name="reg"),
    path('',SignView.as_view(),name="login"),
    path('logout/',Signout.as_view(),name="signout"),
    path('index/',TaskView.as_view(),name="index"),
    path('index/updt/<int:pk>',TaskUpdate.as_view(),name="updt"),
    path('index/delete/<int:pk>',TaskDelete.as_view(),name="del"),
    path('index/edit/<int:pk>',TaskEdit.as_view(),name="edit"),
    path('api/',include("api.urls")),

]
