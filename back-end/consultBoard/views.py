from django.http import HttpResponse
from urllib.parse import unquote

from .models import *
from .serializers import *

from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import *


# 게시판 2 관련 기능


# 게시글을 고를 수 있도록 제목을 포함한 일부 데이터들 전달
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
    
# 게시글 구분ID(pk)를 입력, 해당하는 게시글의 본문 내용 포함 전달
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


# 게시글 검색
# 입력받은 대상과 항목을 입력받아 해당하는 게시글들을 전달
class BoardSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        
        # 대상이 제목일 경우
        if self.kwargs['searchfield'] == 'title':
            
            queryset = BoardConsult.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        # 대상이 내용일 경우
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = BoardConsult.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'board_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        # 대상이 작성자일 경우
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
    
    
    
# 게시글 작성 기능
# 게시글 구분ID로 대상 선택, 게시글 형식에 맞는 데이터를 입력받아 DB에 저장, 게시글 생성
class BoardPostCreateView(generics.CreateAPIView):

    serializer_class = BoardPostCreateSerializer
        
    def perform_create(self, serializer):
        
        BoardConsult.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=user.objects.get(username = "jinwon97")
        )
        
        
        
# 게시글 수정 기능
# 게시글 구분ID로 대상 선택, 형식에 맞는 새 데이터를 입력받아 기존 내용 교체
class BoardPostUpdateView(generics.UpdateAPIView):

    serializer_class = BoardPostUpdateSerializer
    queryset = BoardConsult.objects.all()
    
    def perform_update(self, serializer):                
        instance = self.get_object() 
        
        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']
        instance.save()

        return Response({'success':'create post success'}, status.HTTP_201_CREATED)
    
    
    
# 게시글 삭제 기능
# 게시글 구분ID로 대상 선택, 대상 게시글을 삭제
class BoardPostDeleteView(generics.DestroyAPIView):
    queryset = BoardConsult.objects.all()
    serializer_class = BoardPostSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        instance.delete()
        
        return Response({'success':'delte success'})

# 댓글 조회 기능
# 게시글 구분ID로 대상 선택, 해당 게시글의 댓글들을 전달
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
    
    
    
# 댓글 생성 기능
# 게시글 구분ID(pk)에 형식에 맞는 입력을 받아 새 댓글을 생성
class BoardPostCommentCreateView(generics.CreateAPIView):

    serializer_class = BoardPostcommentCreateSerializer
        
    def perform_create(self, serializer):
        board_id = BoardConsult.objects.get(board_id=self.kwargs['pk'])
        
        CommentsConsult.objects.create(
            contents=serializer.validated_data['contents'],
            user=user.objects.get(username = "jinwon97"),
            board=board_id,
        )



# 댓글 수정 기능
# 댓글 구분ID(pk)와 내용입력, 대상 댓글의 내용 교체
class BoardPostCommentUpdateView(generics.UpdateAPIView):

    serializer_class = BoardPostCommentUpdateSerializer
    queryset = CommentsConsult.objects.all()
    
    def perform_update(self, serializer):
        instance = self.get_object()
        

        instance.contents = serializer.validated_data['contents']
        instance.save()
        return Response({'success' : 'update comment success'}, status.HTTP_200_OK)
    

# 댓글 삭제 기능
# 댓글 구분ID(pk) 입력, 대상 댓글 삭제
class BoardPostCommentDeleteView(generics.DestroyAPIView):

    queryset = CommentsConsult.objects.all()
    
    def delete(self, reqeust, *args, **kwags):
        instance = self.get_object()
        
        
        instance.delete()
        return Response({'success' : 'delete comment success'}, status.HTTP_200_OK)
    


