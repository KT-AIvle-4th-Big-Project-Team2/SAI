import logging
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import UserCustom
from .serializers import *

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from account.customlibs.checkLogin import *


logger = logging.getLogger(__name__)  # 로그를 남길 로거 객체 생성

class SignInView(APIView):
    serializer_class = SignInSerializer
    
    def post(self, request):
        input_data = self.request.data
        passwordAgain = input_data.pop("password_again")
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
        
        if len(passwordAgain) > 25:
            raise ValidationError({'error':'input value format error'}) 
        
        if password != passwordAgain: return Response({'error' : 'two passwords doesnt match'})
        
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error':'username already exists'})
        
        else:
            user = UserCustom.objects.create_user(username = username, password = password, name = name, email = email, 
                                            phonenumber = phonenumber, age = age, gender = gender)
            user.save()
            return Response({'success': "User created successfully"})




class LoginView(APIView):
    serializer_class = LoginSerializer
    
    def post(self, request, format=None):
        try:
            serialized = self.serializer_class(data=request.data)
            if serialized.is_valid():
                username = serialized.validated_data['username']
                password = serialized.validated_data['password']

                user_info = authenticate(username=username, password=password)
                if user_info != None:
                    #auth.login(request, user_info) # session 필요 함수 대체
                    instance = UserCustom.objects.get(username = username)
                    instance.is_active = 1
                    instance.save()
                    
                    logger.debug(f"User {username} logged in successfully")  # 로그 남기기
                    return Response({'success': 'login successful'}, status=status.HTTP_200_OK)
                else:
                    logger.error(f"Login failed for user {username}")  # 로그 남기기
                    return Response({'error': 'wrong user info'})
            else:
                logger.error("Invalid input data during login")  # 로그 남기기
                return Response({'error': 'input value error'})
        except Exception as e:
            logger.exception("An exception occurred during login")  # 예외 발생 시 로그 남기기
            return Response({'error': 'An error occurred during login'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        
               
class LogoutView(APIView):
    def post(self, request, format = None):
        username = self.request.data.pop("username")
        try:
            #auth.logout(request)
            instance = UserCustom.objects.get(usrename = username)
            instance.is_active = 0
            instance.save()
            
            logger.debug(f"User {username} logged out successfully")  # 로그 남기기
            return Response({'success':'logout success'})
        except:
            logger.exception("An exception occurred during login")
            return Response({'error':'logout failed'})



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
        
        
                    
class GetUserView(APIView):
    serializer_class = GetUserData 

    def post(self, request, format=None):
        username = self.request.data.pop("username")
        
        if username:
            instance = UserCustom.objects.get(username=username)
            if user_data.is_valid():
                serializer = self.serializer_class(user_data)
                return Response({serializer.data}, status.HTTP_200_OK)
            else:
                return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)



# @method_decorator(csrf_protect, name='dispatch')
class UpdatePWView(generics.UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdatePWSerializer
    
    def patch(self, request, *args, **kwargs):
        
        username = self.request.data.pop('username')
        
        try:
            instance = UserCustom.objects.get(username = username)
            
        except:
            return Response({'error':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                userIstance.set_password(serializer.validated_data['password'])
            except:
                return Response({'error':'pw input failed'}, status.HTTP_400_BAD_REQUEST)
            userIstance.save()
            return Response({'success':'pw update success'}, status.HTTP_200_OK)
        
        else:
            return Response({serializer.errors}, status.HTTP_400_BAD_REQUEST)



class CheckPWView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PasswordCheckSerializer
    
    def post(self, request):
        username = self.request.user.username
        
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
    
    


class ResetPW(APIView):
    serializer_class = ResetPasswordInput

    def post(self, request):
        try:
            password_again = self.request.data.pop('password_again')
        except:
            raise ValidationError({'error':'input error'}, status.HTTP_400_BAD_REQUEST)
        
        input_data = self.serializer_class(data = request.data)
        
        if not input_data.is_valid(): 
            print(input_data.errors) 
            return Response({"error":"input data error"})
        username = input_data.validated_data['username']
        new_password = input_data.validated_data['password']
        email = input_data.validated_data['email']
        phonenumber = input_data.validated_data['phonenumber']
        
        if new_password != password_again: raise ValidationError({'error':'password not match'}, status.HTTP_400_BAD_REQUEST)
        try:
            instance = UserCustom.objects.get(username = username, phonenumber = phonenumber, email = email)
            instance.set_password(new_password)
            instance.save()
            return Response({'success':'password change success'})
        except:
            return Response({'error':'matching user not found'})