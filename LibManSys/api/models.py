from django.db import models

book_types = (
    ('Phylosophy', 'Phylosophy'),
    ('Novel', 'Novel'),
    ('Poetry', 'Poetry')
    ('Fiction', 'Fiction'),
    ('Biography', 'Biography'),
    ('Testbook', 'TextBook'),
    ('Other', 'Other'),
)


# Create your models here.
class Book(models.Model):
    book = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50, choices=book_types)
    is_issued = models.BooleanField(default=True)
