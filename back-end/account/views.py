import logging
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import UserCustom
from .serializers import *

# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate
from account.customlibs.checkLogin import *


logger = logging.getLogger(__name__)  # 로그를 남길 로거 객체 생성



class SignInView(APIView): # 회원가입
    serializer_class = SignInSerializer
    
    def post(self, request):
        input_data = self.request.data

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
            raise ValidationError({'error':'input value format error'})
        
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error':'username already exists'})
        
        else:
            user = UserCustom.objects.create_user(username = username, password = password, name = name, email = email, 
                                            phonenumber = phonenumber, age = age, gender = gender)
            user.save()
            return Response({'success': "User created successfully"})



class LoginView(APIView): # 로그인
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    
    def post(self, request, format = None):
        serialized = self.serializer_class(data = request.data)
        if serialized.is_valid():
            username = serialized.validated_data['username']
            password = serialized.validated_data['password']
            
            #user_info = authenticate(username=username, password=password)
            
            if True != None:

                return Response({'success' : 'login successful', "username" : username}, status=status.HTTP_202_ACCEPTED) # 로그인에 성공하면 앞으로 유저인증을 위한 키 값(일단은 username)을 전송
            else:
                  return Response({'error' : 'wrong user info'})
        else:
            return Response({'error':'input value error'})
class LogoutView(APIView):
    
    def post(self, request, format = None):
        try:     
            return Response({'success':'logout success'})
        except:
            return Response({'error':'logout failed'})




class FindIDView(APIView):
    permission_classes = (permissions.AllowAny,)
    queryset = UserCustom.objects.all()
    
    serializer_class = FindIDInputSerializer
    
    def post(self, request):
        self.queryset
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            inputs = serializer_data.validated_data
            email = inputs['email']
            phonenumber = inputs['phonenumber']
            try:
                matchingUser = UserCustom.objects.get(email = email, phonenumber = phonenumber)
                matchingUserDatas = FindIDOutputSerializer(matchingUser, many = True)
                return Response({"success" : "ID found", "ID" : matchingUserDatas.validated_data['username']}, 
                                status=status.HTTP_200_OK)
            except:
                raise ValidationError({'message':'matching user not found!'})
        return  Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ResetPW(APIView):
    serializer_class = ResetPasswordInput
    
    def post(self, request):
        input_data = self.serializer_class(data = request.data)
        if not input_data.is_valid(): return Response({"error":"input data error"})
        username = input_data.validated_data['username']
        password = input_data.validated_data['password']
        email = input_data.validated_data['email']
        phonenumber = input_data.validated_data['phonenumber']
        
        try:
            instance = UserCustom.objects.get(username = 'jinwon97')
            instance.set_password(password)
            instance.save()
            return Response({'success':'password change success'})
        except:
            return Response({'error':'matching user not found'})
        





class DeleteAccountView(APIView):
    serializer_class = PasswordCheckSerializer
    
    def delete(self, request):
        username = request.data.pop('username')
        serializer = self.serializer_class(data = request.data)
        
        
        if serializer.is_valid():
            try:
                instance = UserCustom.objects.get(username = username)                
            except:
                return Response({"error":"user doesn't exists error"})
            
            if check_password(serializer.validated_data['password'], instance.password ):
                instance.delete()
                return Response({"success":"user deleted"})
            
            else:
                return Response({'error':'password is wrong'})
            
        else:
            return Response(serializer.errors)
        
        
class UpdatePWView(generics.UpdateAPIView):

    serializer_class = UpdatePWSerializer
    
    def patch(self, request, *args, **kwargs):
        
        username = "jinwon97"
        try:
            instance = UserCustom.objects.get(username = username)
            
        except:
            return Response({'error':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                instance.set_password(serializer.validated_data['password'])
            except:
                return Response({'error':'pw input failed'}, status.HTTP_400_BAD_REQUEST)
            
            instance.save()
            
            return Response({'success':'pw update success'}, status.HTTP_200_OK)
        
        else:
            return Response({serializer.errors}, status.HTTP_400_BAD_REQUEST)



class CheckPWView(APIView):

    serializer_class = PasswordCheckSerializer
    
    def post(self, request):

        username = 'jinwon97'
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            try:
                instance = UserCustom.objects.get(username = username)
            except:
                return Response({"error":"user info error"})
            
            if check_password(serializer.validated_data['password'], instance.password ):
                return Response({'success':'password check success'})
            else:
                return Response({'error':'password is wrong'})
        else:
            return Response({"error":"user info error"})
        
        
        
class FindIDView(APIView):
    queryset = UserCustom.objects.all()
    serializer_class = FindIDInputSerializer
    
    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        
        if serializer_data.is_valid():
            inputs = serializer_data.validated_data
            email = inputs['email']
            phonenumber = inputs['phonenumber']
            
            try:
                # print(email)
                # print(phonenumber)
                matchingUser = UserCustom.objects.get(email = email, phonenumber = phonenumber)
                
                return Response({"success" : "ID found", "ID" : matchingUser.username}, 
                                status=status.HTTP_200_OK)
            except:
                raise ValidationError({'message':'matching user not found!'})
        return  Response({'message':'input error'}, status=status.HTTP_400_BAD_REQUEST)
    
    




             
class GetUserView(APIView):

    serializer_class = GetUserData 

    def post(self, request, format=None):

        username = 'jinwon97'
        if username:
            instance = UserCustom.objects.get(username=username)
            if instance.is_valid():
                serializer = self.serializer_class(instance)
                return Response({serializer.data}, status.HTTP_200_OK)
            else:
                return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)



# class ResetPW(APIView):
#     serializer_class = ResetPasswordInput

#     def post(self, request):
#         try:
#             password_again = self.request.data.pop('password_again')
#         except:
#             raise ValidationError({'error':'input error'}, status.HTTP_400_BAD_REQUEST)
        
#         input_data = self.serializer_class(data = request.data)
        
#         if not input_data.is_valid(): 
#             print(input_data.errors) 
#             return Response({"error":"input data error"})
#         username = input_data.validated_data['username']
#         new_password = input_data.validated_data['password']
#         email = input_data.validated_data['email']
#         phonenumber = input_data.validated_data['phonenumber']
        
#         if new_password != password_again: raise ValidationError({'error':'password not match'}, status.HTTP_400_BAD_REQUEST)
#         try:
#             instance = UserCustom.objects.get(username = username, phonenumber = phonenumber, email = email)
#             instance.set_password(new_password)
#             instance.save()
#             return Response({'success':'password change success'})
#         except:
#             return Response({'error':'matching user not found'})