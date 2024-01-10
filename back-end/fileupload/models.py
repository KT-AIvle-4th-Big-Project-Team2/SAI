# models.py
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_on = models.CharField(max_length=255, default="")  # 여기에 적절한 기본값을 설정하세요.

    def __str__(self):
        return self.file.name


class Uploaded(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_on.date()