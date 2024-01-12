from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import unquote
from rest_framework import generics

from .models import *
from .serializers import *

from rest_framework import generics, permissions
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .serializers import *

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# from django.contrib.auth.models import User
# from django.contrib import auth
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse

from account.customlibs.checkLogin import *

#******************************************************************************************************************************************************************
# 게시글 기능
#******************************************************************************************************************************************************************
    
class BoardPostListView(generics.ListAPIView):
    def get_queryset(self):
        board_contents = BoardConsult.objects.values(
            'board_id',
            'title',
            'creationdate',
            'user__username',
        )
        
        queryset = board_contents
        return queryset
    
    serializer_class = BoardPostListSerializer
    
class BoardPostView(generics.ListAPIView):
    
    def get_queryset(self):

        board_id = self.kwargs['pk']
        queryset = BoardConsult.objects.filter(board_id=board_id).values(
            'board_id',
            'title',
            'contents',
            'creationdate',
            'user__username',
        )
        
        return queryset

    serializer_class = BoardPostSerializer

class BoardSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = BoardConsult.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = BoardConsult.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        elif self.kwargs['searchfield'] == 'name':
            
            queryset = BoardConsult.objects.filter(user__username__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        else:
            return HttpResponse("ERROR")
        
        
        return queryset

    serializer_class = BoardSearchSerializer

class BoardPostCreateView(generics.CreateAPIView):
    serializer_class = BoardPostCreateSerializer
        
    def perform_create(self, serializer):
        key = self.request.data.get("key")
        # self.request.data.pop("key")
        if not LoginCheck(key): raise ValidationError({"error":"user info error"})
        
        user_instance = user.objects.get(username=self.request.data.get('username'))
        
        BoardConsult.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=user_instance
        )
        
class BoardPostUpdateView(generics.UpdateAPIView):#PATCH method
    serializer_class = BoardPostUpdateSerializer
    queryset = BoardConsult.objects.all()
    def perform_update(self, serializer):    
        
        key = self.request.data.get("key")
        if not LoginCheck(key): raise ValidationError({"error":"user info error"})
        
        user_instance = user.objects.get(username = key)
            
        instance = self.get_object() # 입력(pk) 값으로 필터링해 대상 설정. 기본 대상은 테이블의 PK. 두 개 이상 또는 PK말고 다른 걸로 할 시 get_object 함수를 오버라이딩해야함.
        if instance.user_id != user_instance.user_id: raise ValidationError({'error':'wrong user error'})
        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()

class BoardPostDeleteView(generics.DestroyAPIView):
    queryset = BoardConsult.objects.all()
    serializer_class = BoardPostSerializer
    def delete(self, request, *args, **kwargs):
        key = request.data.get("key")
        if not LoginCheck(key) : raise ValidationError({"error":"user info error"})
        
        user_instance = user.objects.get(username = key)
        instance = self.get_object()
        if instance.user_id != user_instance.user_id:  raise ValidationError({'error':'wrong user error'})
        instance.delete()
        return Response({'success':'delte success'})
    
    

#******************************************************************************************************************************************************************
# 댓글 기능
#******************************************************************************************************************************************************************

class BoardPostCommentView(generics.ListAPIView):
    
    def get_queryset(self):

        board_id = self.kwargs['pk']
        queryset = CommentsConsult.objects.filter(board=board_id).values(
            'contents',
            'creationdate',
            'user__username',
            'comment_id',
        )
        
        return queryset

    serializer_class = BoardPostCommentSerializer
    
class BoardPostCommentCreateView(generics.CreateAPIView):

    serializer_class = BoardPostcommentCreateSerializer
        
    def perform_create(self, serializer):
        key = self.request.data.get('key')
        if not LoginCheck(key) :  raise ValidationError({"error":"user info error"})
        
        user_instance = user.objects.get(name=serializer.validated_data.get('name', ''))
        board_id = BoardConsult.objects.get(board_id=self.kwargs['pk'])
        
        CommentsConsult.objects.create(
            contents=serializer.validated_data['contents'],
            user=user_instance,
            board=board_id,
        )

class BoardPostCommentUpdateView(generics.UpdateAPIView):#PATCH method
    serializer_class = BoardPostCommentUpdateSerializer
    
    queryset = CommentsConsult.objects.all()
    
    def perform_update(self, serializer):
        key = self.request.data.get('key')
        if not LoginCheck(key) :  raise ValidationError({"error":"user info error"})    
        user_instance = user.objects.get(username = key)
            
        instance = self.get_object()

        instance.contents = serializer.validated_data['contents']

        instance.save()

class BoardPostDeleteView(generics.DestroyAPIView):
    queryset = BoardConsult.objects.all()
    serializer_class = BoardPostSerializer
    def delete(self, request, *args, **kwargs):
        key = request.data.get("key")
        if not LoginCheck(key) :  raise ValidationError({"error":"user info error"})
        
        user_instance = user.objects.get(username = key)
        instance = self.get_object()
        if instance.user_id != user_instance.user_id:  raise ValidationError({'error':'wrong user error'})
        instance.delete()
        return Response({'success':'delete success'})