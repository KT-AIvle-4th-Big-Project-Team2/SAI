# views.py
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import *

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 파일 업로드
class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FileDownloadView(APIView):
    def get(self, request, file_id):
        try:
            uploaded_file = UploadedFile.objects.get(pk=file_id)
        except UploadedFile.DoesNotExist:
            return Response({'error': '파일을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        with open(uploaded_file.file.path, 'rb') as file:
            response = HttpResponse(file.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
            return response

class FileDownloadAPIView(APIView):
    def get(self, request, pk, format=None):
        uploaded_file = UploadedFile.objects.get(pk=pk)
        serializer = FileDownloadSerializer(uploaded_file)
        return Response(serializer.data)