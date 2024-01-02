from rest_framework import serializers
from .models import *

from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()
    # def to_representation(self, instance):
    #     return {
    #         'post_id': instance['board_id'],
    #         'title': instance['title'],
    #         'tag': instance['tag'],
    #         'date': instance['creationdate'],
    #         'name': instance['user__name']
    #     }
    # class Meta:
    #     model = User
    #     fields = ('name', 'password')
    

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'password', 'email', 'phonenumber', 'age', 'gender']
        
class FindIDInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phonenumber', 'gender']
class FindIDOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']
        
class FindPasswordInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    email = serializers.CharField(max_length=254)
    phonenumber = serializers.CharField(max_length=11)
    gender = serializers.CharField(max_length=1)
    
                                   
class FindPasswordOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
        
class UpdateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    password = serializers.CharField(max_length=75)
    email = serializers.CharField(max_length=254)
    phonenumber = serializers.CharField(max_length=11)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=1)

class PasswordCheckSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    password = serializers.CharField(max_length=75)
    
class DeleteUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)