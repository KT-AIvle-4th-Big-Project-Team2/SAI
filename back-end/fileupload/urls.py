from django.urls import path
from .views import FileUploadAPIView, ImageUploadAPIView
app_name = 'api'
urlpatterns = [
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
]