from rest_framework import serializers
from .models import Announcements, user
        
class AnnouncementListSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            'announcement_id': instance['announcement_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__username']
        }

class AnnouncementSerializer(serializers.Serializer):
    
    def to_representation(self, instance):
        return {
            'announcement_id': instance['announcement_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['admin__username']
        }

class AnnouncementSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'announcement_id': instance['announcement_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__username'],
        }
    class Meta:
        model = Announcements
        fields = ['announcement_id', 'title', 'creationdate', 'admin__username']

class AnnouncementCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    contents = serializers.CharField()
    
    class Meta:
        model = Announcements
        fields = ('title', 'contents')

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ('title', 'contents')