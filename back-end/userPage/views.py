from account.models import *
from board.models import *
from consultBoard.models import *
from faq.models import *
from suggestions.models import *
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# 유저의 개인 데이터 관리 페이지


# 댓글조회
# 유저가 여러 게시판과 글에서 작성한 댓글들을 한 곳에서 조회
class WrittenCommentView(APIView):
    serializer_class = PostCommentSerializer
    
    # user id로 게시판들에서 대상 검색
    def get(self, *args, **kwargs):
        user_id = UserCustom.objects.filter(username = kwargs['username']).values('user_id')[0].get('user_id')

        queryset1 = Comments.objects.filter(user_id = user_id)
        queryset2 = CommentsConsult.objects.filter(user_id = user_id)
        
        # 전체 직렬화
        serializedComments1 = self.serializer_class(queryset1, many = True) 
        serializedComments2 = self.serializer_class(queryset2, many = True)
        
        # 게시판 구분을 위해 원 게시판 붙임
        fullList = serializedComments1.data
        for i in fullList:
            i['board_name'] = 'board'
        
        fullList2 = serializedComments2.data
        for i in fullList2:
            i['board_name'] = "consult board"
        
        # 전달을 위해 묶음
        fullList.extend(fullList2)
        
        return Response(fullList, status.HTTP_200_OK)
    
