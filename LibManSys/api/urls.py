from django.urls import path
from . import views

#Function based view urls
urlpatterns = [
    path('addbook/', views.AddBook, name='createentry'),
    path('allbooks/', views.AllBooks, name='read'),
    path('updatebook/<int:pk>/', views.UpdateBook, name='update'),
    path('deletebook/<int:pk>/', views.DeleteBook, name='delete'),
    ]


#class based views urls
urlpatterns+=[
    path('listcreate/', views.ListCreateView.as_view()), #urls for getall and post method
    path('getupdatedelete/<int:pk>/', views.RetriveUpdateDeleteView.as_view()), #urls for get,put,delete
]

