# urls.py
from django.urls import path
from .views import FileUploadAPIView

urlpatterns = [
    # 파일 업로드 경로 설정
    path('upload/', FileUploadAPIView.as_view(), name='file'),
    
]
