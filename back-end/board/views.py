from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Board
from .serializers import *

class ListPost(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    
class CustomSerializer1(generics.ListAPIView):
    def get_queryset(self):
        board_contents = Board.objects.values(
            'board_id',
            'title',
            'tag',
            'creationdate',
            'user__name',
        )
        print(board_contents)
        
        queryset = board_contents
        return queryset
    
    serializer_class = BoardPostListSerializer
    