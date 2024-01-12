from .models import *
from .serializers import *
from account.models import UserCustom
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from rest_framework import generics

from urllib.parse import unquote


# 자주뭍는 질문게시판  관련 기능

# FAQ 리스트 조회
# FAQ를 고를 수 있도록 일부(제목, 작성자, 작성일)을 
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

# FAQ 내용 조회
# FAQ 구분 ID(pk) 입력, 대상 FAQ 내용 전달
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

# FAQ 검색기능
# FAQ 검색 항목 및 값 입력, 조건에 해당하는 FAQ들을 전달
class FaqSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        
        # FAQ 검색 항목 선택
        # 항목이 제목일 경우
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Faq.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__username',
            )
        
        # 항목이 내용일 경우
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Faq.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        else:# 입력 값의 선택지가 없을 경우 에러 전달.
            raise ValidationError({'error' : 'input error'}, status.HTTP_404_NOT_FOUND)
        
        return queryset

    serializer_class = FaqSearchSerializer


# FAQ 생성기능
# FAQ 형식에 맞는 데이터 입력, 새 데이터 FAQ를 DB에 생성

class FaqCreateView(generics.CreateAPIView):

    serializer_class = FaqCreateSerializer
        
    def perform_create(self, serializer):
        
        Faq.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin = UserCustom.objects.get(username = "jinwon97")
        )
        

# FAQ 수정기능
# 기존FAQ를 구분 ID로 선택, 새로운 내용으로 교체
class FaqUpdateView(generics.UpdateAPIView):#PATCH method
    #permission_classes = (permissions.IsAdminUser,)
    serializer_class = FaqUpdateSerializer
    queryset = Faq.objects.all()
    
    def perform_update(self, serializer):    
        instance = self.get_object()
        
        # if serializer.is_valid() != True : raise ValidationError({'error' : 'update announcement failed'}, status.HTTP_400_BAD_REQUEST)
        
        # 입력 값에서 존재 또는 공란이 아닌 항목만 입력
        if 'title' in serializer.validated_data:
            if serializer.validated_data['title'] != '':
                instance.title = serializer.validated_data['title']
        
        if 'contents' in serializer.validated_data:
            
            if serializer.validated_data['contents'] != '':
                instance.contents = serializer.validated_data['contents']

        instance.save()
        
        return Response({'success':'update faq success'}, status.HTTP_200_OK)




# FAQ 삭제
# FAQ 구분ID(pk)로 선택, 대상을 삭제
class FaqDeleteView(generics.DestroyAPIView):

    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    
    def delete(self, request, *args, **kwargs):
        
        instance = self.get_object()
        instance.delete()
        
        return Response({'success':'delete success'})