# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.contrib.auth import authenticate, login
# from rest_framework import viewsets
# from rest_framework import permissions
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound

from .models import UserAccount
from .serializers import UserModelSerializer

@api_view(['GET'])
def UserView(request):
    user_details = User.objects.all()
    serialized_data = UserModelSerializer(user_details, many=True)
    
    return Response(serialized_data.data)
        
@api_view(['POST'])
def CreateUser(request):
    user_name = request.data['user_name']
    password = request.data['password']
    if UserAccount.objects.filter(name=user_name).exists():
        return Response('User name already exists', status=status.HTTP_404_NOT_FOUND)
    else:
        user = UserAccount(name=user_name, password=password)
        user.save()
        return Response('User created successfully', status=200)

# @api_view(['GET'])
# def GetUser(request):
#     user_name = request.GET.get('user_name')
#     password = request.GET.get('password')
#     user = UserModel.objects.filter(name=user_name)
#     if user.exists():
#         # serialized_data = serializers.serialize("json",user)
#         return Response(user.get)        

#     # if user.exists():
#     #     if(user.)
#     #     return Response('User name already exists')
#     # else:
#     #     user = UserModel(name=user_name, password=password)
#     #     user.save()
#     #     return Response('User created successfully', status=200)
