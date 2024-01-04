from rest_framework import serializers
from .models import *
        
class FaqListSerializer(serializers.Serializer):
    faq_id = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateTimeField()
    name = serializers.IntegerField()
    
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__username']
        }

class FaqSerializer(serializers.Serializer):
    faq_id = serializers.IntegerField()
    title = serializers.CharField()
    contents = serializers.CharField()
    date = serializers.DateTimeField()
    name = serializers.IntegerField()
    
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'name': instance['admin__username']
        }
class FaqSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__username']
        }
    class Meta:
        model = Faq
        fields = ['faq_id', 'title', 'creationdate', 'admin__username']

class FaqCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    contents = serializers.CharField()
    username = serializers.CharField()
    
    class Meta:
        model = Faq
        fields = ('title', 'contents', 'username')
class FaqUpdateSerializer(serializers.Serializer):

    title = serializers.CharField()
    contents = serializers.CharField()