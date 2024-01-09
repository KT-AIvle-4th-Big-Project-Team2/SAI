from django.urls import path
from .views import FileUpload
app_name = 'api'
urlpatterns = [
    path('uploadfile/', FileUpload.as_view(), name='upload-file'),
]