from .models import *
from .serializers import *
from account.models import UserCustom

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics

from urllib.parse import unquote

#******************************************************************************************************************************************************************
# 공지글 기능
#******************************************************************************************************************************************************************



class AnnouncementListView(generics.ListAPIView):

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
    
    def get_queryset(self):
        if self.kwargs['searchfield'] == 'title':

            queryset = Announcements.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Announcements.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        elif self.kwargs['searchfield'] == 'admin':
            
            queryset = Announcements.objects.filter(user__username__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
        else:
            raise ValidationError({'error':'search field error'}, status.HTTP_404_NOT_FOUND)
        return queryset
    
    


class AnnouncementCreateView(APIView):

    serializer_class = AnnouncementCreateSerializer
    
    def post(self, request, serializer):
        if not UserCustom.objects.get(self.request.data.get("username")).is_superuser: return Response({'error' : 'no auth'}, status.HTTP_401_UNAUTHORIZED)
        
        Announcements.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin=UserCustom.objects.get(username = self.request.data.get("username"))
        )
        
        
        

class AnnouncementUpdateView(generics.UpdateAPIView):

    serializer_class = AnnouncementUpdateSerializer
    queryset = Announcements.objects.all()
    
    def perform_update(self, request):    
        if not UserCustom.objects.get(self.request.data("username")).is_superuser: return Response({'error' : 'no auth'}, status.HTTP_401_UNAUTHORIZED)
        instance = self.get_object()
        
        serializer = self.serializer_class(data = self.request.data, partial = True)
        
        if serializer.is_valid() != True : raise ValidationError({'error' : 'update announcement failed'}, status.HTTP_400_BAD_REQUEST)
        
        if 'title' in serializer.validated_data:
            
            if serializer.validated_data['title'] != '':
                instance.title = serializer.validated_data['title']
        
        if 'contents' in serializer.validated_data:
            
            if serializer.validated_data['contents'] != '':
                instance.contents = serializer.validated_data['contents']

        instance.save()
        
        return Response({'success':'update announcement success'}, status.HTTP_200_OK)
    
    
    

class AnnouncementdeleteView(APIView):

    queryset = Announcements.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        if not UserCustom.objects.get(self.request.data("username")).is_superuser: return Response({'error' : 'no auth'}, status.HTTP_401_UNAUTHORIZED)
        instance = Announcements.objects.get(kwargs['pk'])
        
        instance.delete()
        
        return Response({'success' : 'delete announcement success'}, status.HTTP_200_OK)