from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import LoginSerializer, RegistrationSerializer
import requests

def index(request):
    response = requests.request("GET", 'http://127.0.0.1:8001/api/allbooks/')
    data=response.json()
    return render(request,'allbooks.html',{'list':data})

class Registration(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self,request,formate=None):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg': 'Registeration is Done ! Please Login'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class Login(generics.GenericAPIView,APIView):
  queryset = User.objects.all()
  serializer_class = LoginSerializer

  def post(self, request, format=None):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    if not User.objects.get(email=email).exist():
        return Response({'msg':'Oops ! You are not registered yet'},status=status.HTTP_404_NOT_FOUND)
    if User.objects.get(email=email,password=password).exist():
        return Response({'msg':'Email Or Password is Incorrect'},status=status.HTTP_404_NOT_FOUND)
    return Response({'msg':'Login Successfully'}, status=status.HTTP_200_OK)
