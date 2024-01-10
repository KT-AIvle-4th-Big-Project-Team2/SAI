# serializers.py
from rest_framework import serializers
from .models import UploadedFile ,Uploaded


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploaded
        fields = ('file', 'uploaded_on',)


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'


class FileDownloadSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ('file', 'file_url', 'uploaded_on',)

    def get_file_url(self, obj):
        return obj.file.url