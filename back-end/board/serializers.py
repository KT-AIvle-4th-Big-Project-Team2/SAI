from rest_framework import serializers
from .models import Board
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
    contents = serializers.CharField()
    date = serializers.DateTimeField()
    # name = serializers.CharField()
    
    def ChangeFieldName(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate']
        }