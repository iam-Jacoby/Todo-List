from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from reminder.models import Task
from api.serializer import TaskSerializer,userserializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
# Create your views here.

authentication_Classes=[authentication.BasicAuthentication]
permission_classes=[permissions.IsAuthenticated]

class TaskViewsetView(ViewSet):
    def list (self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializers=TaskSerializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializers=TaskSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return Response()
    # return Response("Login user doesnt match")





                        #   25 / 03 / 2024
    
class SignupView(APIView):
    def post(self,request,*args,**kwargs):
        # username,pwd,email
        serializer=userserializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()   # modelserializer
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)