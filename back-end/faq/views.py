from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import *
from .serializers import *

#******************************************************************************************************************************************************************
# 게시글 기능
#******************************************************************************************************************************************************************
    
class FaqListView(generics.ListAPIView):
    def get_queryset(self):
        board_contents = Faq.objects.values(
            'faq_id',
            'title',
            'creationdate',
            'admin__admin_id',
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
            'admin__admin_id',
        )
        
        return queryset

    serializer_class = FaqSerializer

class FaqSearchView(generics.ListAPIView):
    
    def get_queryset(self):
        board_id = self.kwargs['searchfield']
        if self.kwargs['searchfield'] == 'title':
            
            queryset = Faq.objects.filter(title__contains=self.kwargs['searchkeyword']).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__admin_id',
            )
            
        elif self.kwargs['searchfield'] == 'contents':
            
            queryset = Faq.objects.filter(contents__contains=self.kwargs['searchkeyword']).values(
                'faq_id',
                'title',
                'creationdate',
                'admin__admin_id',
            )
            
        else:
            return HttpResponse("ERROR")
        
        
        print(queryset)
        return queryset

    serializer_class = FaqSearchSerializer

class FaqCreateView(generics.CreateAPIView):
    serializer_class = FaqCreateSerializer
        
    def perform_create(self, serializer):
        # admin_instance = Admin.objects.get(admin_id=serializer.validated_data.get('admin_id', ''))
        #print(admin_instance)
        Faq.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin_id = serializer.validated_data['admin_id'],
        )
        
class FaqUpdateView(generics.UpdateAPIView):#PATCH method
    serializer_class = FaqUpdateSerializer
    queryset = Faq.objects.all()
    def perform_update(self, serializer):    
        instance = self.get_object() # 입력(pk) 값으로 필터링해 대상 설정. 기본 대상은 테이블의 PK. 두 개 이상 또는 PK말고 다른 걸로 할 시 get_object 함수를 오버라이딩해야함.

        instance.title = serializer.validated_data['title']
        instance.contents = serializer.validated_data['contents']

        instance.save()

class FaqDeleteView(generics.DestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer