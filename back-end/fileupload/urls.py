# urls.py
from django.urls import path
from .views import FileUploadView, FileDownloadView , FileUploadAPIView , FileDownloadAPIView

urlpatterns = [
    # 파일 업로드
    path('upload/', FileUploadAPIView.as_view(), name='file'),
    
    
    path('file-upload/', FileUploadView.as_view(), name='file-upload'),
    path('file-download/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),
    path('file-download-api/<int:pk>/', FileDownloadAPIView.as_view(), name='file-download-api'),
]
