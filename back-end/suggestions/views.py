from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import *
from .serializers import *
    
    
class SuggestionListView(generics.ListAPIView):
    def get_queryset(self):
        suggestion_contents = Suggestions.objects.values(
            'suggestion_id',
            'title',
            'creationdate',
            'user__name',
        )
        
        queryset = suggestion_contents
        return queryset
    
    serializer_class = SuggestionListSerializer
    
class SuggestionView(generics.ListAPIView):
    
    def get_queryset(self):

        suggestion_id = self.kwargs['pk']
        queryset = Suggestions.objects.filter(suggestion_id=suggestion_id).values(
            'suggestion_id',
            'title',
            'contents',
            'creationdate',
            'user__name',
        )
        
        return queryset

    serializer_class = SuggestionSerializer

class SuggestionSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Suggestions.objects.filter(title__contains=self.kwargs['searchkeyword']).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__name',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Suggestions.objects.filter(contents__contains=self.kwargs['searchkeyword']).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__name',
            )
            
        elif self.kwargs['searchfield'] == 'name':
            
            queryset = Suggestions.objects.filter(user__name__contains=self.kwargs['searchkeyword']).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__name',
            )
            
        else:
            return HttpResponse("ERROR")
        
        
        print(queryset)
        return queryset

    serializer_class = SuggestionSearchSerializer

class SuggestionCreateView(generics.CreateAPIView):
    serializer_class = SuggestionCreateSerializer
        
    def perform_create(self, serializer):
        user_instance = User.objects.get(name=serializer.validated_data.get('name', ''))
        
        Suggestions.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=user_instance
        )
        
class SuggestionUpdateView(generics.UpdateAPIView):
    serializer_class = SuggestionUpdateSerializer
    queryset = Suggestions.objects.all()
    def perform_update(self, serializer):    
        instance = self.get_object()

        instance.title = serializer.validated_data['title']
        instance.tag = serializer.validated_data['tag']
        instance.contents = serializer.validated_data['contents']

        instance.save()