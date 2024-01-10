from django.shortcuts import render
from django.http import HttpResponse

from urllib.parse import unquote

from account.models import UserCustom
from .models import *
from .serializers import *

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .serializers import *

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
    
    
    

class BoardPostCreateView(APIView):

    serializer_class = BoardPostCreateSerializer
    
    def post(self, serializer):
        try: self.request.data.get("username")
        except: return Response({'error':'input data error'}, status.HTTP_400_BAD_REQUEST)
        BoardConsult.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=UserCustom.objects.get(self.request.data.get("username"))
        )
        return Response({'success':'post create success'}, status.HTTP_200_OK)
        

class BoardPostUpdateView(APIView):
    serializer_class = BoardPostUpdateSerializer
    
    def patch(self,request, *args, **kwargs):                
        
        username = self.request.data.pop('username')
        instance = BoardConsult.objects.get(board_id = kwargs['pk'])
        
        if instance.user__username != username: return Response({'error':'wrong user error'}, status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            instance.title = serializer.validated_data['title']
            instance.contents = serializer.validated_data['contents']
            instance.save()
            return Response({'success':'create post success'}, status.HTTP_201_CREATED)
        else:
            return Response({'error':'input data error'}, status.HTTP_400_BAD_REQUEST)



class BoardPostDeleteView(APIView):
    serializer_class = BoardPostSerializer
    
    def post(self, request, *args, **kwargs):
        instance = BoardConsult.objects.get(board_id = kwargs['pk'])
        if instance.user__username != self.request.data.get('username'):  return Response({'error':'wrong user error'})
        
        instance.delete()
        
        return Response({'success':'delte success'})
    
    
class BoardPostDeleteView(generics.DestroyAPIView):

    serializer_class = BoardPostSerializer
    queryset = BoardConsult.objects.all()
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.user != self.request.user:  raise ValidationError({'error':'wrong user error'}, status.HTTP_401_UNAUTHORIZED)
        
        instance.delete()
        
        return Response({'success':'delete success'}, status.HTTP_200_OK)

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
    
    
    
# @method_decorator(csrf_protect, name='dispatch')
class BoardPostCommentCreateView(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BoardPostcommentCreateSerializer
        
    def perform_create(self, serializer):
        board_id = BoardConsult.objects.get(board_id=self.kwargs['pk'])
        
        CommentsConsult.objects.create(
            contents=serializer.validated_data['contents'],
            user=self.request.user,
            board=board_id,
        )



# @method_decorator(csrf_protect, name='dispatch')
class BoardPostCommentUpdateView(generics.UpdateAPIView):#PATCH method
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BoardPostCommentUpdateSerializer
    queryset = CommentsConsult.objects.all()
    
    def perform_update(self, serializer):
        instance = self.get_object()
        
        if instance.user != self.request.user: raise ValidationError({'error':'wrong user error'}, status.HTTP_401_UNAUTHORIZED)
        instance.contents = serializer.validated_data['contents']
        instance.save()
        return Response({'success' : 'update comment success'}, status.HTTP_200_OK)
    
    
# @method_decorator(csrf_protect, name='dispatch')
class BoardPostCommentDeleteView(generics.DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = CommentsConsult.objects.all()
    
    def delete(self, reqeust, *args, **kwags):
        instance = self.get_object()
        
        if instance.user != UserCustom.objects.get(username = "jinwon97"): raise ValidationError({'error':'wrong user error'}, status.HTTP_403_FORBIDDEN)
        
        instance.delete()
        return Response({'success' : 'delete comment success'}, status.HTTP_200_OK)
    


