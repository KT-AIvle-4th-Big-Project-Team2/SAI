from rest_framework import serializers
from .models import file



class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']









# class fileSerializer(serializers.Serializer):
#     file_id = serializers.IntegerField()
#     name = serializers.CharField()
#     creationdate = serializers.DateTimeField()
#     url = serializers.CharField()
    
#     def to_representation(self, instance):
#         return {
#             'post_id': instance['board_id'],
#             'title': instance['title'],
#             'date': instance['creationdate'],
#             'name': instance['user__name']
#         }
