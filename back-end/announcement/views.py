from .models import *
from .serializers import *

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth.models import User
    
class AnnouncementListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        announcement_contents = Announcements.objects.values(
            'announcement_id',
            'creationdate',
            'title',
            'admin__username',
        )
        
        queryset = announcement_contents
        return queryset
    
    serializer_class = AnnouncementListSerializer
    
class AnnouncementView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        print(self.kwargs['pk'])
        announcement_id = self.kwargs['pk']
        
        queryset = Announcements.objects.filter(announcement_id=announcement_id).values(
            'announcement_id',
            'title',
            'contents',
            'creationdate',
            'admin__username',
        )
        return queryset

    serializer_class = AnnouncementSerializer

class AnnouncementSearchView(generics.ListAPIView):
    serializer_class = AnnouncementSearchSerializer
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        print(self.kwargs['searchfield'])
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':

            queryset = Announcements.objects.filter(title__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Announcements.objects.filter(contents__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        elif self.kwargs['searchfield'] == 'admin':
            
            queryset = Announcements.objects.filter(user__username__contains=self.kwargs['searchkeyword']).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
        return queryset

@method_decorator(csrf_protect, name='dispatch')
class AnnouncementCreateView(generics.CreateAPIView):

    serializer_class = AnnouncementCreateSerializer
        
    def perform_create(self, serializer):
        user_instance = user.objects.get(username=self.request.user)
        
        Announcements.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin=user_instance
        )
        
@method_decorator(csrf_protect, name='dispatch')
class AnnouncementUpdateView(generics.UpdateAPIView):
    serializer_class = AnnouncementUpdateSerializer
    queryset = Announcements.objects.all()
    
    def perform_update(self, serializer):    
        instance = self.get_object()

        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()
@method_decorator(csrf_protect, name='dispatch')
class AnnouncementdeleteView(generics.DestroyAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer