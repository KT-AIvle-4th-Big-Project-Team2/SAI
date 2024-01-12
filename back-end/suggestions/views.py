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
    
# 제안사항 관련 기능

# 제안사항 목록 조회
# 제안사항을 고를 수 있도록 제목, 작성일, 작성자만 전달하는 기능
class SuggestionListView(generics.ListAPIView):
    def get_queryset(self):
        suggestion_contents = Suggestions.objects.values(
            'suggestion_id',
            'title',
            'creationdate',
            'user__username',
        )
        
        queryset = suggestion_contents
        return queryset
    
    serializer_class = SuggestionListSerializer
    
    
# 제안사항 읽기
# 제안사항 구분ID(pk)에 해당하는 제안사항 글의 내용을 전달
class SuggestionView(generics.ListAPIView):
    
    def get_queryset(self):

        suggestion_id = self.kwargs['pk']
        queryset = Suggestions.objects.filter(suggestion_id=suggestion_id).values(
            'suggestion_id',
            'title',
            'contents',
            'creationdate',
            'user__username',
        )
        
        return queryset

    serializer_class = SuggestionSerializer


# 제안사항 검색
# 항목과 값을 입력, 항목의 내용이 입력 값에 해당되는 제안사항들을 전달
class SuggestionSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        
        # 검색 항목 설정
        # 항목이 제목일 경우
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Suggestions.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        # 항목이 내용일 경우
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Suggestions.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__username',
            )
        # 항목이 작성자일 경우
        elif self.kwargs['searchfield'] == 'name':
            
            queryset = Suggestions.objects.filter(user__username__contain=unquote(self.kwargs['searchkeyword'])).values(
                'suggestion_id',
                'title',
                'creationdate',
                'user__username',
            )
            
        else:# 해당하는 항목이 없을 시 에러 메시지 전달.
            raise ValidationError({'error':'search field error'}, status.HTTP_404_NOT_FOUND)
        
        return queryset

    serializer_class = SuggestionSearchSerializer


# 제안사항 작성
# 제안사항 형식에 맞는 데이터를 입력, DB에 저장해 제안사항 생성
class SuggestionCreateView(generics.CreateAPIView):

    serializer_class = SuggestionCreateSerializer
        
    def perform_create(self, serializer):
        
        Suggestions.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin=UserCustom.objects.get(username = "jinwon97")
        )
        
        
# 제안사항 수정
# 기존 제안사항을 구분ID(pk)로 조회, 대상의 내용을 새 내용으로 대체
class SuggestionUpdateView(generics.UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SuggestionUpdateSerializer
    queryset = Suggestions.objects.all()
    
    def perform_update(self, serializer):    
        instance = self.get_object()

        # if instance.user != self.request.user : raise ValidationError({'error':'not the user'}, status.HTTP_403_FORBIDDEN)
        
        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()
        
        
# 제안사항 삭제
# 제안사항 구분ID(pk)로 조회, 대상을 삭제
class SuggestionDeleteView(generics.DestroyAPIView):

    queryset = Suggestions.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        instance.delete()
    
        return Response({'success' : 'delete announcement success'}, status.HTTP_200_OK)