from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Board
from .serializers import BoardSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer