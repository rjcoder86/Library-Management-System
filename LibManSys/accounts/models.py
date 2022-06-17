from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField( max_length=255, unique=True)
    password=models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
