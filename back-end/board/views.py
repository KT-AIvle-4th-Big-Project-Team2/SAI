from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.

from .models import Board
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

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
    
class CustomSerializer2(generics.ListAPIView):
    
    def get_queryset(self):

        board_id = self.kwargs['pk']
        queryset = Board.objects.filter(board_id=board_id).values(
            'board_id',
            'title',
            'tag',
            'contents',
            'creationdate',
            'user__name',
        )
        
        print(queryset)
        return queryset

    serializer_class = BoardPostSerializer
    
class CustomSerializer3(generics.CreateAPIView):
    parser_classes = [JSONParser]
    serializer_class = BoardPostCreateSerializer
        
    def perform_create(self, serializer):
        user_instance = User.objects.get(name=serializer.validated_data.get('name', ''))
        
        Board.objects.create(
            title=serializer.validated_data['title'],
            tag=serializer.validated_data['tag'],
            contents=serializer.validated_data['contents'],
            user=user_instance
        )
    