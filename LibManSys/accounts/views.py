from django.contrib.auth import authenticate
from rest_framework import status, generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserManager
from .serializer import LoginSerializer, RegistrationSerializer
from api import permissions

class Registration(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAll,)

    def post(self,request,formate=None):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({ 'msg': 'Registeration is Done ! Please Login'}, status=status.HTTP_201_CREATED)
        return Response({'msg':'Email already exist '},status=status.HTTP_404_NOT_FOUND)


class Login(generics.GenericAPIView,APIView):
  queryset = User.objects.all()
  serializer_class = LoginSerializer
  permission_classes = (permissions.AllowAll,)

  def post(self, request, format=None):
      serializer = LoginSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      email = serializer.data.get('email')
      password = serializer.data.get('password')
      user = authenticate(email=email, password=password)
      print(user,email,password)
      if user is None:
          return Response({'msg': 'Email or password is incorrect'}, status=status.HTTP_404_NOT_FOUND)
      return Response({'msg': 'Login Successfully', 'is_admin': user.is_admin}, status=status.HTTP_200_OK)


