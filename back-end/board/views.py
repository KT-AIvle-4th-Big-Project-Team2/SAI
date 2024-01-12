from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import unquote
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .serializers import *
from account.models import UserCustom
    

# 게시판 1 관련 기능



# 게시글을 고를 수 있도록 제목, 작성자, 작성일 전송
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


# 게시글 구분 id(board_id) 전송 시 해당 게시글 본문 내용 전송
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


# 게시글 검색 영역 및 대상 입력 시 조건에 맞는 게시글 전송
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
    
    

# 게시글 쓰기
# 게시글 내용을 입력받아 DB에 저장
class BoardPostCreateView(generics.CreateAPIView):
    
    serializer_class = BoardPostCreateSerializer
        
    def perform_create(self, serializer):
        
        Board.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            user=UserCustom.objects.get(username= self.request.data.get('username'))
        )
            
        return Response({'success': 'create post success'})



# 게시글 수정
# 새 내용을 입력받아 기존 게시글의 내용을 교체
class BoardPostUpdateView(generics.UpdateAPIView):

    serializer_class = BoardPostUpdateSerializer
    queryset = Board.objects.all()
    
    def perform_update(self, serializer):
            
        instance = self.get_object() 
        
        # serializer로 유효성 검사, 실패. 응답 전송
        if  serializer.is_valid() != True: return Response({'input format error'}, status.HTTP_400_BAD_REQUEST)
        
        # 입력받은 요청자의 username이 게시글의 작성자와 불일치시 실패. 응답 전송
        if instance.user__username != serializer.validated_data['username']:
            return Response({'user not correct'}, status.HTTP_403_FORBIDDEN)
        
        # 입력받은 데이터 중 있는 데이터만 입력
        if serializer.validated_data['title'] != "":
            instance.name = serializer.validated_data['title']
        if serializer.validated_data['contents'] != "":
            instance.password = serializer.validated_data['contents']
        
        instance.save()
        return Response({'success': 'update post success'}, status.HTTP_201_CREATED)
        
        


class BoardPostDeleteView(generics.DestroyAPIView):

    queryset = Board.objects.all()
    
    def delete(self, request, *args, **kwargs):

        instance = self.get_object()
        
        instance.delete()
        
        return Response({'success':'delte success'}, status.HTTP_200_OK)

        
# 보안 적용 문제로 못 쓰게 된 게시글 삭제 코드
# @method_decorator(csrf_protect, name='dispatch')
# class BoardPostDeleteView(APIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Board.objects.all()
#     serializer_class = BoardPostSerializer
    
#     def delete(self, request, *args, **kwargs):
#         # username = self.request.user.username
#         username = self.request.data.get("username")
#         instance = self.get_object()
#         instance.delete()
        # if instance.user != UserCustom.objects.get(username = "username"):  
        #     return Response({'error':'wrong user error'}, status = status.HTTP_403_FORBIDDEN)
        # else:
        #     instance.delete()
            
        #     return Response({'success':'delte success'}, status.HTTP_200_OK)
        # # if instance.user != self.request.user:  
        #     return Response({'error':'wrong user error'}, status = status.HTTP_403_FORBIDDEN)
        # else:
        #     instance.delete()
            
        #     return Response({'success':'delte success'}, status.HTTP_200_OK)
    


# 게시글 댓글 조회 기능
class BoardPostCommentView(generics.ListAPIView):
    def get_queryset(self):

        # 게시글의 고유 ID를 입력받아 해당 게시글의 댓글들을 전송
        board_id = self.kwargs['pk']
        queryset = Comments.objects.filter(board=board_id).values(
            'contents',
            'creationdate',
            'user__username',
            'comment_id',
        )
        
        return queryset

    serializer_class = BoardPostCommentSerializer
    


# 게시글 댓글 작성 기능
class BoardPostCommentCreateView(generics.CreateAPIView):

    serializer_class = BoardPostcommentCreateSerializer
    
    # 게시글의 고유 ID(pk)로 게시글을 찾은 후
    # 새 댓글의 내용을 입력받아 등록
    def perform_create(self, serializer):
        board_id = Board.objects.get(board_id=self.kwargs['pk'])
        
        Comments.objects.create(
            contents=serializer.validated_data['contents'],

            user = UserCustom.objects.get(username = serializer.validated_data['username']),
            board=board_id,
        )
        return Response({'success': 'crate comment success'}, status.HTTP_201_CREATED)

# 게시글 댓글 수정 기능
class BoardPostCommentUpdateView(generics.UpdateAPIView):

    serializer_class = BoardPostCommentUpdateSerializer
    
    # 댓글의 구분 ID를 입력받아 대상을 정하고, 입력받은 새 내용으로 대체
    queryset = Comments.objects.all()
    
    def perform_update(self, serializer):

        instance = self.get_object()
        

        
        instance.contents = serializer.validated_data['contents']

        instance.save()

# 게시글 댓글 삭제 기능
class BoardPostCommentDeleteView(generics.DestroyAPIView):

    queryset = Comments.objects.all()
    
    # 댓글의 구분 ID를 입력받아, 대상을 삭제
    def delete(self, request, *args, **kwargs):
    
        instance = self.get_object()

        
        instance.delete()
        return Response({'success':'delete success'}, status.HTTP_200_OK)