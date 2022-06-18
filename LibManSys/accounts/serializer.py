from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields=['email', 'first_name','last_name','is_admin', 'password']
    extra_kwargs={
      'password':{'write_only':True}
    }


class LoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']