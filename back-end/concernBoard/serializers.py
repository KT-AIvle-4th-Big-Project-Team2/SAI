from rest_framework import serializers
from .models import BoardConcern, CommentsConcern
        
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
        
class BoardPostCommentSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['user__name'],
            'comment_id': instance['comment_id']
        }

class BoardSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'tag': instance['tag'],
            'date': instance['creationdate'],
            'name': instance['user__name']
        }
    class Meta:
        model = BoardConcern
        fields = ['post_id', 'title', 'tag', 'creationdate', 'user__name']

class BoardPostCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    tag = serializers.CharField()
    contents = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = BoardConcern
        fields = ('title', 'tag', 'contents', 'name')

class BoardPostUpdateSerializer(serializers.Serializer):

    title = serializers.CharField()
    tag = serializers.CharField()
    contents = serializers.CharField()

        
class BoardPostcommentCreateSerializer(serializers.ModelSerializer):

    contents = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = CommentsConcern
        fields = ('contents', 'name')


class BoardPostCommentUpdateSerializer(serializers.ModelSerializer):

    contents = serializers.CharField()
    
    class Meta:
        model = CommentsConcern
        fields = ('contents',)