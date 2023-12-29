from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.

from .models import Board
from .serializers import *
from rest_framework.response import Response

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
    
    serializer_class = BoardPostCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
