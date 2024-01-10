from django.db import models
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    pthto = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("gallery:image_list")
    
