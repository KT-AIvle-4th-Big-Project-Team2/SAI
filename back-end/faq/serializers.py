from rest_framework import serializers
from .models import *
        
class FaqListSerializer(serializers.Serializer):
    faq_id = serializers.IntegerField()
    title = serializers.CharField()
    date = serializers.DateTimeField()
    admin_id = serializers.IntegerField()
    
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'admin_id': instance['admin__admin_id']
        }

class FaqSerializer(serializers.Serializer):
    faq_id = serializers.IntegerField()
    title = serializers.CharField()
    contents = serializers.CharField()
    date = serializers.DateTimeField()
    admin_id = serializers.IntegerField()
    
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'contents': instance['contents'],
            'date': instance['creationdate'],
            'admin_id': instance['admin__admin_id']
        }
class FaqSearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'faq_id': instance['faq_id'],
            'title': instance['title'],
            'date': instance['creationdate'],
            'admin_id': instance['admin__admin_id']
        }
    class Meta:
        model = Faq
        fields = ['faq_id', 'title', 'creationdate', 'admin__admin_id']

class FaqCreateSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    contents = serializers.CharField()
    admin_id = serializers.IntegerField()
    
    class Meta:
        model = Faq
        fields = ('title', 'contents', 'admin_id')
class FaqUpdateSerializer(serializers.Serializer):

    title = serializers.CharField()
    contents = serializers.CharField()