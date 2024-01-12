from rest_framework import serializers
from .models import Board, Comments
        
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
            'date': instance['creationdate'],
            'name': instance['user__username']
        }

class BoardPostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    title = serializers.CharField()
    contents = serializers.CharField()
    date = serializers.DateTimeField()
    name = serializers.CharField()
    
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['user__username']
        }
        
class BoardPostCommentSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['user__username'],
            'comment_id': instance['comment_id']
        }

class BoardSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'post_id': instance['board_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['user__username']
        }
    class Meta:
        model = Board
        fields = ['post_id', 'title', 'creationdate', 'user__username']

class BoardPostCreateSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Board
        fields = ['title', 'contents', 'username']

class BoardPostUpdateSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=False, allow_blank  = True)
    contents = serializers.CharField(required=False, allow_blank  = True)
    username = serializers.CharField(max_length = 30)
    class Meta:
        model = Comments
        fields = ["title", "contents", "username"]
        
class BoardPostcommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('contents','username')


class BoardPostCommentUpdateSerializer(serializers.ModelSerializer):

    contents = serializers.CharField()
    
    class Meta:
        model = Comments
        fields = ('contents')
        
        
# class GetUserData(serializers.ModelSerializer):
#     class Meta:
#         model = UserCustom
#         fields = ['username', 'email', 'phonenumber', 'age', 'gender']