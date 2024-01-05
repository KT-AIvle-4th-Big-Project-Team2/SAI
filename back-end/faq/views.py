from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import unquote

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import *
from account.customlibs.checkLogin import *
#******************************************************************************************************************************************************************
# 게시글 기능
#******************************************************************************************************************************************************************
    
class FaqListView(generics.ListAPIView):
    def get_queryset(self):
        board_contents = Faq.objects.values(
            'faq_id',
            'title',
            'creationdate',
            'admin__username',
        )
        
        queryset = board_contents
        return queryset
    
    serializer_class = FaqListSerializer
    
class FaqView(generics.ListAPIView):
    
    def get_queryset(self):

        faq_id = self.kwargs['pk']
        queryset = Faq.objects.filter(faq_id=faq_id).values(
            'faq_id',
            'title',
            'contents',
            'creationdate',
            'admin__username',
        )
        
        return queryset

    serializer_class = FaqSerializer

class FaqSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Faq.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Faq.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        else:
            return HttpResponse("ERROR")
        
        
        print(queryset)
        return queryset

    serializer_class = FaqSearchSerializer

class FaqCreateView(generics.CreateAPIView):
    serializer_class = FaqCreateSerializer
        
    def perform_create(self, serializer):
        
        key = self.request.data.get("key")
        # self.request.data.pop("key")
        if not LoginCheck(key, True): 
            raise ValidationError({"error":"user info error"})
        
        admin_instance = Admin.objects.get(username=serializer.validated_data.get('username', ''))
        Faq.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin = admin_instance,
        )
        
class FaqUpdateView(generics.UpdateAPIView):#PATCH method
    serializer_class = FaqUpdateSerializer
    queryset = Faq.objects.all()
    def perform_update(self, serializer):    
        
        key = self.request.data.get("key")
        # self.request.data.pop("key")
        if not LoginCheck(key, True): raise ValidationError({"error":"user info error"})
        
        user_instance = Admin.objects.get(username = key)
        instance = self.get_object()
        if instance.admin_id != user_instance.user_id: raise ValidationError({'error':'wrong user error'})
        
        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()

class FaqDeleteView(generics.DestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    def delete(self, request, *args, **kwargs):
        key = request.data.get("key")
        if not LoginCheck(key, True) : raise ValidationError({"error":"user info error"})

        user_instance = Admin.objects.get(username = key)
        instance = self.get_object()
        if instance.admin_id != user_instance.user_id: raise ValidationError({'error':'wrong user error'})
        instance.delete()
        return Response({'success':'delte success'})