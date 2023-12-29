from rest_framework import serializers
from .models import Board, User
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'board_id',
            'title',
            'contents',
            'tag',
            'user',
        )
        model = Board
        
class BoardPostListSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    title = serializers.CharField()
    post_tag = serializers.CharField()
    date = serializers.DateTimeField()
    name = serializers.CharField()
    
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'post_tag' : instance['tag'],
            'date': instance['creationdate'],
            'name': instance['user__name']
        }

class BoardPostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    title = serializers.CharField()
    tag = serializers.CharField()
    contents = serializers.CharField()
    date = serializers.DateTimeField()
    name = serializers.CharField()
    
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'tag': instance['tag'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['user__name']
        }

class BoardPostCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    tag = serializers.CharField()
    contents = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = Board
        fields = ('title', 'tag', 'contents', 'name')
