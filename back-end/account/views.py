import logging
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import UserCustom
from .serializers import *

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from account.customlibs.checkLogin import *


logger = logging.getLogger(__name__)  # 로그를 남길 로거 객체 생성



class SignInView(APIView): # 회원가입
    serializer_class = SignInSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            password = serializer.validated_data['password'] 
            email = serializer.validated_data['email']
            phonenumber = serializer.validated_data['phonenumber']
            age = serializer.validated_data['age']
            gender = serializer.validated_data['gender']
            
        else:
            raise ValidationError({'error':'input value format error'},status.HTTP_400_BAD_REQUEST)
        
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error':'username already exists'}, status.HTTP_400_BAD_REQUEST)
        
        else:
            user = UserCustom.objects.create_user(username = username, password = password, name = name, email = email, 
                                            phonenumber = phonenumber, age = age, gender = gender)
            user.save()
            return Response({'success': "User created successfully"}, status=status.HTTP_200_OK)



class LoginView(APIView): # 로그인
    serializer_class = LoginSerializer
    
    def post(self, request, format = None):
        serialized = self.serializer_class(data = request.data)
        if serialized.is_valid():
            username = serialized.validated_data['username']
            password = serialized.validated_data['password']
            
            user_info = authenticate(username=username, password=password)
            
            if user_info != None:

                return Response({'success' : 'login successful'}, status=status.HTTP_200_OK)
            else:
                  return Response({'error' : 'wrong user info'}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'input value error'}, status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView): # 로그아웃
    
    def post(self, request, format = None):
        try:     
            return Response({'success':'logout success'}, status.HTTP_200_OK)
        except:
            return Response({'error':'logout failed'}, status.HTTP_200_OK)




class FindIDView(APIView): # 아이디 찾기
    queryset = UserCustom.objects.all()
    
    serializer_class = FindIDInputSerializer
    
    def post(self, request):
        self.queryset
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            email = serializer_data.validated_data['email']
            phonenumber = serializer_data.validated_data['phonenumber']
            try:
                matchingUser = UserCustom.objects.get(email = email, phonenumber = phonenumber)
                matchingUserDatas = FindIDOutputSerializer(matchingUser, many = True)
                return Response({"ID" : matchingUserDatas.validated_data['username']}, 
                                status=status.HTTP_200_OK)
            except:
                raise ValidationError({'message':'matching user not found!'}, status.HTTP_400_BAD_REQUEST)
        return  Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ResetPW(APIView): # 비밀번호 찾기(리셋)
    serializer_class = ResetPasswordInput
    
    def post(self, request):
        input_data = self.serializer_class(data = request.data)
        if input_data.is_valid() != True: 
            return Response({"error":"input data error"}, status.HTTP_400_BAD_REQUEST)
        
        username = input_data.validated_data['username']
        password = input_data.validated_data['password']
        email = input_data.validated_data['email']
        phonenumber = input_data.validated_data['phonenumber']
        
        try:
            instance = UserCustom.objects.get(username = username, email = email, phonenumber = phonenumber)
        except:
            raise ValidationError({'message':'matching user not found!'}, status.HTTP_400_BAD_REQUEST)
        
        instance.password = make_password(password)
        instance.save()
                
        return Response({'success':'password change success'}, status.HTTP_200_OK)





class CheckPWView(APIView): # 비밀번호 인증

    serializer_class = PasswordCheckSerializer
    
    def post(self, request):
        username = self.request.data.pop("username")
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            try:
                instance = UserCustom.objects.get(username = username)
            except:
                return Response({"error":"user info error"}, status.HTTP_400_BAD_REQUEST)
            
            if check_password(serializer.validated_data['password'], instance.password ):
                return Response({'success':'password check success'})
            else:
                return Response({'error':'password is wrong'})
        else:
            return Response({"error":"user info error"})


        
        
class UpdateUserInfo(generics.UpdateAPIView): # 수정

    serializer_class = SignInSerializer
    
    def post(self, request, *args, **kwargs):
        
        username = self.request.data.pop("username")
        instance = UserCustom.objects.get(username = username)
        
        serializer = self.serializer_class(self.request.data, partial = True)
        
        if serializer.is_valid() != True: return Response({'error':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            if 'name' in serializer.validated_data:
                instance.name = serializer.validated_data['name']
            if 'password' in serializer.validated_data:
                instance.set_password(serializer.validated_data['password'])
            if 'email' in serializer.validated_data:
                instance.email = serializer.validated_data['email']
            if 'phonenumber' in serializer.validated_data:
                instance.phonenumber = serializer.validated_data['phonenumber']
            if 'age' in serializer.validated_data:
                instance.age = serializer.validated_data['age']
            if 'gender' in serializer.validated_data:
                instance.gender = serializer.validated_data['gender']
        
        instance.save()



class DeleteAccountView(APIView): # 회원탈퇴
    
    def delete(self, request):
        username = request.data.pop('username')
        
        try:
            targetUser = UserCustom.objects.get(username = username)
        except:
            return Response({'error':'no  match user'}, status.HTTP_400_BAD_REQUEST)
        
        targetUser.delete()
        return Response({'success':'user delete success'}, status.HTTP_200_OK)
        

             
class GetUserView(APIView): # 유저정보 불러오기
    serializer_class = GetUserData 

    def post(self, request, format=None):
        username = self.request.data.pop('username')
        
        instance = UserCustom.objects.get(username=username)
        if instance.is_valid():
            serializer = self.serializer_class(instance)
            return Response({serializer.data}, status.HTTP_200_OK)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)