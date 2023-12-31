from rest_framework import serializers
from .models import Announcements, Admin
        
class AnnouncementListSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            'announcement_id': instance['announcement_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__name']
        }

class AnnouncementSerializer(serializers.Serializer):
    
    def to_representation(self, instance):
        return {
            'announcement_id': instance['announcement_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['admin__name']
        }

class BoardSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__name'],
        }
    class Meta:
        model = Announcements
        fields = ['announcement_id', 'title', 'creationdate', 'admin__name']

class AnnouncementCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    contents = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = Announcements
        fields = ('title', 'contents', 'name')
