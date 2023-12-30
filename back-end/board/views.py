from django.shortcuts import render
from rest_framework import generics, status
from django.http import HttpResponse
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
    
    
class BoardPostListView(generics.ListAPIView):
    def get_queryset(self):
        board_contents = Board.objects.values(
            'board_id',
            'title',
            'tag',
            'creationdate',
            'user__name',
        )
        
        queryset = board_contents
        return queryset
    
    serializer_class = BoardPostListSerializer
    
class BoardPostView(generics.ListAPIView):
    
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

class BoardSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        print(self.kwargs['searchfield'])
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Board.objects.filter(title__contains=self.kwargs['searchkeyword']).values(
                'board_id',
                'title',
                'tag',
                'creationdate',
                'user__name',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Board.objects.filter(contents__contains=self.kwargs['searchkeyword']).values(
                'board_id',
                'title',
                'tag',
                'creationdate',
                'user__name',
            )
            
        elif self.kwargs['searchfield'] == 'name':
            
            queryset = Board.objects.filter(user__name__contains=self.kwargs['searchkeyword']).values(
                'board_id',
                'title',
                'tag',
                'creationdate',
                'user__name',
            )
            
        else:
            return HttpResponse("ERROR")
        
        
        print(queryset)
        return queryset

    serializer_class = BoardSearchSerializer

class BoardPostCreateView(generics.CreateAPIView):
    #parser_classes = [JSONParser]
    serializer_class = BoardPostCreateSerializer
        
    def perform_create(self, serializer):
        user_instance = User.objects.get(name=serializer.validated_data.get('name', ''))
        
        Board.objects.create(
            title=serializer.validated_data['title'],
            tag=serializer.validated_data['tag'],
            contents=serializer.validated_data['contents'],
            user=user_instance
        )
        
    