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
            'name': instance['admin__name']
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
            'name': instance['admin__name']
        }
class FaqSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'name': instance['admin__name']
        }
    class Meta:
        model = Faq
        fields = ['faq_id', 'title', 'creationdate', 'admin__name']

class FaqCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    contents = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = Faq
        fields = ('title', 'contents', 'name')
class FaqUpdateSerializer(serializers.Serializer):

    title = serializers.CharField()
    contents = serializers.CharField()