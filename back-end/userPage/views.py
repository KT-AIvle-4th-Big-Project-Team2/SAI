from django.shortcuts import render
from account.models import *
from board.models import *
from consultBoard.models import *
from faq.models import *
from suggestions.models import *
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

from urllib.parse import unquote




class WrittenCommentView(APIView):
    serializer_class = PostCommentSerializer
    
    def get(self, *args, **kwargs):
        user_id = UserCustom.objects.filter(username = kwargs['username']).values('user_id')[0].get('user_id')
        print(user_id)
        queryset1 = Comments.objects.filter(user_id = user_id)
        queryset2 = CommentsConsult.objects.filter(user_id = user_id)
        
        print(queryset1)
        
        serializedComments1 = self.serializer_class(queryset1, many = True) 
        serializedComments2 = self.serializer_class(queryset2, many = True)
        
        fullList = serializedComments1.data
        for i in fullList:
            i['board_name'] = 'board'
        
        fullList2 = serializedComments2.data
        for i in fullList2:
            i['board_name'] = "consult board"
            
        fullList.extend(fullList2)
        
        return Response(fullList, status.HTTP_200_OK)
    
