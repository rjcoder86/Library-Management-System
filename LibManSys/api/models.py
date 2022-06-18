from django.db import models


# Create your models here.
class Book(models.Model):
    book = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50,default=None)
    is_issued = models.BooleanField(default=True)
