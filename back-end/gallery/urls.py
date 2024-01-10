from django.urls import path
from django.views.generic import ListView , CreateView , DetailView 
from .models import Image


app_name = "gallery"

urlpatterns = [
     path('list/',ListView.as_view(model=Image), name = 'image_list'),
     path('detail/<pk>/',DetailView.as_view(model=Image) , name = "image_detail"),
     path('add/',CreateView.as_view(model=Image, fields= '__all__'),name='image_add'),
     
]