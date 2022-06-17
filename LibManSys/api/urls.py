from django.urls import path
from . import views

urlpatterns = [
    path('addbook/', views.AddBook, name='createentry'),
    path('allbooks/', views.AllBooks, name='read'),
    path('updatebook/<int:pk>/', views.UpdateBook, name='update'),
    path('deletebook/<int:pk>/', views.DeleteBook, name='delete'),
    ]
