from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import Announcements
from .serializers import *

    
class AnnouncementListView(generics.ListAPIView):
    def get_queryset(self):
        announcement_contents = Announcements.objects.values(
            'announcement_id',
            'creationdate',
            'title',
            'admin__name',
        )
        
        queryset = announcement_contents
        return queryset
    
    serializer_class = AnnouncementListSerializer
    
class AnnouncementView(generics.ListAPIView):
    
    def get_queryset(self):
        print(self.kwargs['pk'])
        announcement_id = self.kwargs['pk']
        
        queryset = Announcements.objects.filter(announcement_id=announcement_id).values(
            'announcement_id',
            'title',
            'contents',
            'creationdate',
            'admin__name',
        )
        return queryset

    serializer_class = AnnouncementSerializer

class AnnouncementSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        print(self.kwargs['searchfield'])
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Announcements.objects.filter(title__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__name',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Announcements.objects.filter(contents__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__name',
            )
            
        elif self.kwargs['searchfield'] == 'name':
            
            queryset = Announcements.objects.filter(admin__name__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__name',
            )

    serializer_class = AnnouncementSearchSerializer

class AnnouncementCreateView(generics.CreateAPIView):

    serializer_class = AnnouncementCreateSerializer
        
    def perform_create(self, serializer):
        admin_instance = Admin.objects.get(name=serializer.validated_data.get('name', ''))
        
        Announcements.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin=admin_instance
        )
        
class AnnouncementUpdateView(generics.UpdateAPIView):
    serializer_class = AnnouncementUpdateSerializer
    queryset = Announcements.objects.all()
    
    def perform_update(self, serializer):    
        instance = self.get_object()

        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()
        
class AnnouncementdeleteView(generics.DestroyAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer