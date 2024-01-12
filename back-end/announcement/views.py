from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from urllib.parse import unquote


# 관리자의 공지사항 기능.

# 공지사항 목록 조회
class AnnouncementListView(generics.ListAPIView):

    # 공지사항 조회
    def get_queryset(self):
        announcement_contents = Announcements.objects.values(
            'announcement_id',
            'creationdate',
            'title',
            'admin__username',
        )
        
        # 공지사항 전송
        queryset = announcement_contents
        return queryset
    
    serializer_class = AnnouncementListSerializer
    
    
# 공지사항 내용 조회
class AnnouncementView(generics.ListAPIView):

    # 공지사항 구분번호로 공지사항 선택
    def get_queryset(self):

        announcement_id = self.kwargs['pk']
        
        # 공지사항 내용 전송
        queryset = Announcements.objects.filter(announcement_id=announcement_id).values(
            'announcement_id',
            'title',
            'contents',
            'creationdate',
            'admin__username',
        )
        return queryset
    
    serializer_class = AnnouncementSerializer
    
    
# 공지사항 검색
class AnnouncementSearchView(generics.ListAPIView):
    serializer_class = AnnouncementSearchSerializer
    
    # 공지사항 검색 대상 선택
    def get_queryset(self):
        
        # 공지사항 제목 검색, 쿼리셋 설정
        if self.kwargs['searchfield'] == 'title':
            
            # 공지사항 제목 검색, 쿼리셋 설정
            queryset = Announcements.objects.filter(title__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        # 공지사항 내용 검색
        elif self.kwargs['searchfield'] == 'contents':
            
            # 공지사항 내용 검색, 쿼리셋 설정
            queryset = Announcements.objects.filter(contents__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
            
        # 공지사항 작성 관리자 검색색
        elif self.kwargs['searchfield'] == 'admin':
            
            # 공지사항 작성 관리자 검색, 쿼리셋 설정
            queryset = Announcements.objects.filter(user__username__contains=unquote(self.kwargs['searchkeyword'])).values(
                'announcement_id',
                'title',
                'creationdate',
                'admin__username',
            )
        else:
            # 검색 실패, 응답 전송
            raise ValidationError({'error':'search field error'}, status.HTTP_404_NOT_FOUND)
        
        # 조회 성공, 데이터 전송송
        return queryset
    
    

# 공지사항 작성
class AnnouncementCreateView(generics.CreateAPIView):
    
    serializer_class = AnnouncementCreateSerializer
        
    # 입력 데이터 serializer 입력
    def perform_create(self, serializer):
        
        Announcements.objects.create(
            title=serializer.validated_data['title'],
            contents=serializer.validated_data['contents'],
            admin=user.objects.get(username = "jinwon97")
        )
        
        
        

# 공지사항 수정
class AnnouncementUpdateView(generics.UpdateAPIView):
    
    serializer_class = AnnouncementUpdateSerializer
    queryset = Announcements.objects.all()
    
    def perform_update(self, request):    
        instance = self.get_object()
        
        serializer = self.serializer_class(data = self.request.data, partial = True)
        
        # 입력 데이터 유효성 실패 시 실패 응답 전송
        if serializer.is_valid() != True : raise ValidationError({'error' : 'update announcement failed'}, status.HTTP_400_BAD_REQUEST)
        
        # 해당하는 항목이 유효한 데이터로 존재 시 대상 공지사항에 새로 입력 및 저장
        if 'title' in serializer.validated_data:
            
            if serializer.validated_data['title'] != '':
                instance.title = serializer.validated_data['title']
        
        if 'contents' in serializer.validated_data:
            
            if serializer.validated_data['contents'] != '':
                instance.contents = serializer.validated_data['contents']

        instance.save()
        
        return Response({'success':'update announcement success'}, status.HTTP_200_OK)
    
    
    
# 공지사항 삭제 
class AnnouncementdeleteView(generics.DestroyAPIView):
    
    # 대상 공지사항을 조회해 존재시 삭제.
    queryset = Announcements.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        instance.delete()
        
        return Response({'success' : 'delete announcement success'}, status.HTTP_200_OK)