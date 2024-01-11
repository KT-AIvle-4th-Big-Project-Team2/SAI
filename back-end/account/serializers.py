from rest_framework import serializers
# from .models import Admin, User
from .models import UserCustom

class SignInSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCustom
        fields = ['username', 'name', 'password', 'email', 'phonenumber', 'age', 'gender']
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['email', 'password']

class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username']
        
class FindPwSerialzer(serializers.Serializer):
    username = serializers.CharField(max_length = 30)
    email = serializers.CharField(max_length = 254)
    
        
# class FindIDInputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserCustom
#         fields = ['email', 'phonenumber']
# class FindIDOutputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserCustom
#         fields = ['username']
        
# class FindPasswordInputSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=75)
#     email = serializers.CharField(max_length=254)
#     phonenumber = serializers.CharField(max_length=11)
#     gender = serializers.CharField(max_length=1)
    
                                   
# class FindPasswordOutputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserCustom
#         fields = ['username', 'password', 'email', 'phonenumber', 'age', 'gender']
        
class UpdateUserSerializer(serializers.ModelSerializer):
    
    email = serializers.CharField(required=False, allow_blank  = True)
    password = serializers.CharField(required=False, allow_blank  = True)
    name = serializers.CharField(required=False, allow_blank  = True)
    phonenumber = serializers.CharField(required=False, allow_blank  = True)
    age = serializers.IntegerField(required=False, allow_null  = True)
    gender = serializers.CharField(required=False, allow_blank  = True)

    class Meta:
        model = UserCustom
        fields = ['name', 'email', 'phonenumber', 'age', 'gender', 'password']
        
class UpdatePWSerializer(serializers.Serializer):
    
    password = serializers.CharField(max_length=30)

class PasswordCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['username', 'password']
    
class DeleteUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)

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
