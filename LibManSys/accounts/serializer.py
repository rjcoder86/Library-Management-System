from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields=['email', 'first_name','last_name','is_admin', 'password']
    extra_kwargs={
      'password':{'write_only':True}
    }

    # def save(self, commit=True):
    #   # Save the provided password in hashed format
    #   user = super().save(commit=False)
    #   user.set_password(self.data["password"])
    #   user.save()
    #   return user

    def create(self, validate_data):
      return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']