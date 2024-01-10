from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import unquote
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .serializers import *
from account.models import UserCustom
from rest_framework import status

#******************************************************************************************************************************************************************
# 게시글 기능
#******************************************************************************************************************************************************************
    


class BoardPostListView(generics.ListAPIView):
    
    def get_queryset(self):
        board_contents = Board.objects.values(
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
        queryset = Board.objects.filter(board_id=board_id).values(
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
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Board.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Board.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        elif self.kwargs['searchfield'] == 'username':
            
            queryset = Board.objects.filter(user__username__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        else:
            return Response()
        
        
        return queryset

    serializer_class = BoardSearchSerializer
    
    
    
class BoardPostCreateView(APIView):
    
    serializer_class = BoardPostCreateSerializer
    def post(self, request, serializer):
        
        try:
            userinstance = UserCustom.objects.get(username = self.request.data('username'))
        except:
            return Response({'error':'no user found'}, status.HTTP_400_BAD_REQUEST)
        
        Board.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=UserCustom.objects.get(username = serializer.validated_data['username']),
        )      
        return Response({'success': 'create post success'})



class BoardPostUpdateView(APIView):
    serializer_class = BoardPostUpdateSerializer()
    def patch(self, *args, **kwargs):
        username = self.request.data.pop('username')
        postinstance = Board.objects.get(board_id = kwargs['pk'])
        
        if postinstance.user__username != username: return Response({'error' : 'no auth'}, status.HTTP_403_FORBIDDEN)
            
        serializer = self.serializer_class(data = self.request.data, partial = True)

        if serializer.is_valid() != True: return Response({'error' : 'input data error'}) 

        if "title" in serializer.validated_data:
            postinstance.title = serializer.validated_data['title']
        if "contents" in serializer.validated_data:
            postinstance.contents = serializer.validated_data['contents']
            
        postinstance.save()
        return Response({'success': 'update post success'}, status.HTTP_201_CREATED)
        
        

class BoardPostDeleteView(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            if Board.objects.get(board_id = kwargs['pk']).user__username != self.request.data.get('username'): return Response({'error':'user not match'}, status.HTTP_403_FORBIDDEN)
        except:
            return Response({'error':'input data error'}, status.HTTP_400_BAD_REQUEST)
        Board.objects.get(board_id = kwargs['pk']).delete()
        
        return Response({'succeess':'post deleted'}, status.HTTP_200_OK)
       

#******************************************************************************************************************************************************************
# 댓글 기능
#******************************************************************************************************************************************************************
class BoardPostCommentView(generics.ListAPIView):

    def get_queryset(self):

        board_id = self.kwargs['pk']
        queryset = Comments.objects.filter(board=board_id).values(
            'contents',
            'creationdate',
            'user__username',
            'comment_id',
        )
        
        return queryset

    serializer_class = BoardPostCommentSerializer
    



class BoardPostCommentCreateView(APIView):

    serializer_class = BoardPostcommentCreateSerializer
    
    def post(self, serializer):
        board_id = Board.objects.get(board_id=self.kwargs['pk'])
        username = UserCustom.objects.get(username = self.request.data.pop("username")),
        serializer = self.serializer_class(data = self.requst.data)
        
        Comments.objects.create(
            contents=serializer.validated_data['contents'],
            user = username,
            board=board_id,
            )
        return Response({'success': 'crate comment success'}, status.HTTP_201_CREATED)

class BoardPostCommentUpdateView(generics.UpdateAPIView):#PATCH method

    serializer_class = BoardPostCommentUpdateSerializer
    
    def patch(self, serializer):
        instance = self.get_object()
        username = self.request.data.pop("username")
        # if instance.user != self.request.user: raise ValidationError({'error':'wrong user error'}, status = status.HTTP_403_FORBIDDEN)
        if instance.user__username != username: raise ValidationError({'error':'wrong user error'}, status = status.HTTP_403_FORBIDDEN)
        
        instance.contents = serializer.validated_data['contents']

        instance.save()
        
        return Response({"success":"comment update success"}, status.HTTP_200_OK)

class BoardPostCommentDeleteView(APIView):
    
    def post(self, request, *args, **kwargs):
        instance = Board.objects.get(board_id = self.kwargs['pk'])
        try:
            if instance.user__username != self.request.data.pop("username"): return Response({'error':'wrong user error'}, status = status.HTTP_403_FORBIDDEN)
        except: return Response({'error':'input data error'}, status.HTTP_400_BAD_REQUEST)
        instance.delete()
        
        return Response({'success':'delete success'}, status.HTTP_200_OK)