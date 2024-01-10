from rest_framework import serializers
# from .models import Admin, User
from .models import UserCustom

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username', 'password']
    

class SignInSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCustom
        fields = ['username', 'name', 'password', 'email', 'phonenumber', 'age', 'gender']

    
class FindIDInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['email', 'name']
class FindIDOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username']
        
class FindPasswordInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    email = serializers.CharField(max_length=254)
    phonenumber = serializers.CharField(max_length=11)
    gender = serializers.CharField(max_length=1)
    
                                   
class FindPasswordOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username', 'password', 'email', 'phonenumber', 'age', 'gender']
        
class UpdateUserSerializer(serializers.ModelField):
    class Meta:
        model = UserCustom
        fields = ['username', 'password', 'email', 'phonenumber', 'age', 'gender']
        
class UpdatePWSerializer(serializers.Serializer):
    
    password = serializers.CharField(max_length=20)

class PasswordCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['password']

class GetUserData(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username', 'name', 'email', 'phonenumber', 'age', 'gender']
        
        
class ResetPasswordInput(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 75)
    password = serializers.CharField(max_length = 25)
    class Meta:
        model = UserCustom
        fields = ['username','password', 'email', 'phonenumber']
    
