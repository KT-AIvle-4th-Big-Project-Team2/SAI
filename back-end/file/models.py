from django.db import models

# Create your models here.

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(instance.image_id, extension)

class UploadedImage(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')


class file(models.Model):
    file_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=75)
    fileurl = models.TextField()
    creationdate = models.DateTimeField(auto_now_add = True)

    class Meta:
        managed = False
        db_table = 'file'