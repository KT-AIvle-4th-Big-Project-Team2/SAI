# from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt
from .models import UserCustom
from .serializers import *

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from urllib.parse import unquote
from account.customlibs.checkLogin import *


#logger = logging.getLogger(__name__)  # 로그를 남길 로거 객체 생성

# @method_decorator(ensure_csrf_cookie, name='dispatch') # 바로 아래의 View를 호출하면 CSRF 토큰을 전달하도록 설정        
# class GetCSRFToken(APIView):

#     def get(self, request, format = None):
#         return Response({'success' : 'CSRF Cookie set'})


# @method_decorator(csrf_protect, name='dispatch')
# class CheckAuthenticatedView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
    
#     def get(self, request, format = None):
#         try:
#             isAuthenticated = request.user.is_authenticated
            
#             if isAuthenticated:
#                 return Response({'isAuthenticated':'sucess'})
#             else:
#                 return Response({'isAuthenticated':'error'})
#         except:
#             return Response({'error': 'Something went wrong during checking authentication status'})



# @method_decorator(csrf_protect, name='dispatch')
class SignInView(APIView):
    serializer_class = SignInSerializer
    
    def post(self, request):
        # input_data = self.request.data
        # passwordAgain = input_data.get("password_again")
        # input_data.pop("password_again")
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
            raise ValidationError({'error':serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        # if len(passwordAgain) > 25:
        #     raise ValidationError({'error':'input value format error'}) 
        
        # if password != passwordAgain: return Response({'error' : 'two passwords doesnt match'})
        
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error':'username already exists'})
        
        else:
            user = UserCustom.objects.create_user(username = username, password = password, name = name, email = email, 
                                            phonenumber = phonenumber, age = age, gender = gender)
            user.save()
            return Response({'success': "User created successfully"})



# @method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    serializer_class = LoginSerializer
    
    def post(self, request, format = None):
        serialized = self.serializer_class(data = request.data)
        if serialized.is_valid():
            email = serialized.validated_data['email']
            password = serialized.validated_data['password']
            
            username = UserCustom.objects.get(email = email).username
            
            user_info = authenticate(username = username, password=password)
            if user_info != None:
                # auth.login(request, user_info)
                return Response({'success' : 'login successful', 'username' : username}, status=status.HTTP_200_OK)
            else:
                  return Response({'error' : 'wrong user info'})
        else:
            return Response({'error':'input value error'})


class LogoutView(APIView):
#     # serializer_class = LoginSerializer
    def get(self, request, format = None):
        
        try:
            # UserCustom.objects.get(username = self.request.data.get(username)).is_login = False
            
            return Response({'success':'logout success'})
        except:
            return Response({'error':'logout failed'})


class UpdateUserInfo(generics.GenericAPIView): # 수정
    serializer_class = UpdateUserSerializer

    def patch(self, request, *args, **kwargs):
        
        username = unquote(kwargs['username']) #유저 닉네임은 업데이트 대상이 아님!
        instance = UserCustom.objects.get(username = username)
        
        serializer = self.serializer_class(data = self.request.data, partial = True)
        
        if serializer.is_valid() != True: return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.validated_data['name'] != "":
                instance.name = serializer.validated_data['name']
            if serializer.validated_data['password'] != "":
                instance.password = make_password(serializer.validated_data['password'])
            if serializer.validated_data['email'] :
                instance.email = serializer.validated_data['email']
            if serializer.validated_data['phonenumber'] :
                instance.phonenumber = serializer.validated_data['phonenumber']
            if serializer.validated_data['age'] :
                instance.age = serializer.validated_data['age']
            if serializer.validated_data['gender'] :
                instance.gender = serializer.validated_data['gender']
            instance.save()
            return Response({'user update success'}, status.HTTP_200_OK)


class findPWView(generics.GenericAPIView):
    serializer_class =FindPwSerialzer
    def post(self, request):
        serialized = self.serializer_class(data =request.data)
        if serialized.is_valid():
            
            try:
                UserCustom.objects.get(username = serialized.validated_data['username'], email = serialized.validated_data['email'])
                return Response({'matchig user found email sent'}, status.HTTP_200_OK)
            except:
                return Response(serialized.errors, status.HTTP_404_NOT_FOUND)
        else:
            return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)

class CheckPWView(APIView):
    
    def post(self, request):
        # username = self.request.user.username
        #username = "jinwon97"
        
        serialized = PasswordCheckSerializer(data = request.data)
        
        if serialized.is_valid():
            try:
                instance = UserCustom.objects.get(username = serialized.validated_data["username"])
            except:
                return Response({"error":"user info error"})
            
            if check_password(serialized.validated_data['password'], instance.password ):
                return Response({'success':'password check success'}, status.HTTP_200_OK)
            else:
                return Response({'error':'password is wrong'}, status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error":"user info error"}, status.HTTP_400_BAD_REQUEST)

class GetUserView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GetUserData 

    def get(self, *args, **kwargs):
        
        try:
            user_data = UserCustom.objects.get(username = unquote(kwargs['username']))
            if user_data:
                serializer = self.serializer_class(user_data)
                return Response(serializer.data)
            else:
                return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class DeleteAccountView(APIView):
    def delete(self, *args, **kwargs):
        try:
            UserCustom.objects.get(username = unquote(kwargs["username"]))
            return Response({f"user deleted success"}, status.HTTP_200_OK)
        except:
            return Response({"no username matched"}, status=status.HTTP_400_BAD_REQUEST)        


# @method_decorator(csrf_protect, name='dispatch')        
# class LogoutView(APIView):
#     # serializer_class = LoginSerializer
#     def post(self, request, format = None):
        
#         try:
#             # UserCustom.objects.get(username = self.request.data.get(username)).is_login = False
            
#             return Response({'success':'logout success'})
#         except:
#             return Response({'error':'logout failed'})





# @method_decorator(csrf_protect, name = 'dispatch')
# class DeleteAccountView(APIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = PasswordCheckSerializer
    
#     def delete(self, request):
#         serializer = self.serializer_class(data = request.data)
        
#         if serializer.is_valid():
#             try:
#                 instance = UserCustom.objects.get(username = UserCustom.objects.get(username = "jinwon97").username)
                
#             except:
#                 return Response({"error":"user doesn't exists error"})
            
#             if check_password(serializer.validated_data['password'], instance.password ):
#                 instance.delete()
#                 return Response({"success":"user deleted"})
            
#             else:
#                 return Response({'error':'password is wrong'})
            
#         else:
#             return Response(serializer.errors)
        



        
        
                
# @method_decorator(csrf_protect, name='dispatch')       
# class GetUserView(APIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = GetUserData 

#     def post(self, request, format=None):
#         # username = self.request.data.pop("username")
#         username = UserCustom.objects.get(username = self.request.data.get("username"))
        
#         try:
#             user_data = UserCustom.objects.get(username = username)
#             if user_data:
#                 serializer = self.serializer_class(user_data)
#                 return Response(serializer.data)
#             else:
#                 return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)






# @method_decorator(csrf_protect, name='dispatch')
# class UpdatePWView(generics.UpdateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     # serializer_class = UpdatePWSerializer
    
#     def patch(self, request, *args, **kwargs):
        
#         # user = self.request.user
#         user = UserCustom.objects.get(username = "jinwon97")
        
#         try:
#             userIstance = UserCustom.objects.get(username = user.username)
#         except:
#             return Response({'error':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = UpdatePWSerializer(data = request.data)
#         if serializer.is_valid():
#             try:
#                 userIstance.set_password(serializer.validated_data['password'])
#             except:
#                 return Response({'error':'pw input failed'}, status.HTTP_400_BAD_REQUEST)
#             userIstance.save()
#             return Response({'success':'pw update success'}, status.HTTP_200_OK)
        
#         else:
#             return Response({serializer.errors}, status.HTTP_400_BAD_REQUEST)


# class UpdatePWView(generics.UpdateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     # serializer_class = UpdatePWSerializer
    
#     def patch(self, request, *args, **kwargs):
        
#         # user = self.request.user
#         user = UserCustom.objects.get(username = "jinwon97")
        
#         try:
#             userIstance = UserCustom.objects.get(username = user.username)
#         except:
#             return Response({'error':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = UpdatePWSerializer(data = request.data)
#         if serializer.is_valid():
#             try:
#                 userIstance.set_password(serializer.validated_data['password'])
#             except:
#                 return Response({'error':'pw input failed'}, status.HTTP_400_BAD_REQUEST)
#             userIstance.save()
#             return Response({'success':'pw update success'}, status.HTTP_200_OK)
        
#         else:
#             return Response({serializer.errors}, status.HTTP_400_BAD_REQUEST)




    

        
        
# @method_decorator(csrf_protect, name = 'dispatch')
# class FindIDView(APIView):
#     queryset = UserCustom.objects.all()
#     serializer_class = FindIDInputSerializer
    
#     def post(self, request):
#         serializer_data = self.serializer_class(data=request.data)
        
#         if serializer_data.is_valid():
#             inputs = serializer_data.validated_data
#             email = inputs['email']
#             phonenumber = inputs['phonenumber']
            
#             try:
#                 # print(email)
#                 # print(phonenumber)
#                 matchingUser = UserCustom.objects.get(email = email, phonenumber = phonenumber)
                
#                 return Response({"success" : "ID found", "ID" : matchingUser.username}, 
#                                 status=status.HTTP_200_OK)
#             except:
#                 raise ValidationError({'message':'matching user not found!'})
#         return  Response({'message':'input error'}, status=status.HTTP_400_BAD_REQUEST)
    
    

# @method_decorator(csrf_protect, name = 'dispatch')
# class ResetPW(APIView):
#     serializer_class = ResetPasswordInput

#     def post(self, request):
#         # try:
#         #     # password_again = self.request.data.pop('password_again')
#         # except:
#         #     raise ValidationError({'error':'input error'}, status.HTTP_400_BAD_REQUEST)
        
#         input_data = self.serializer_class(data = request.data)
        
#         if not input_data.is_valid(): 

#             return Response({"error":"input data error"})
#         username = input_data.validated_data['username']
#         new_password = input_data.validated_data['password']
#         email = input_data.validated_data['email']
#         phonenumber = input_data.validated_data['phonenumber']
        
        



# class DeleteAccountView(APIView): # 회원탈퇴
    
#     def delete(self, request, *args, **kwargs):
#         username = kwargs['username']
        
#         # if new_password != password_again: raise ValidationError({'error':'password not match'}, status.HTTP_400_BAD_REQUEST)
#         try:
#             instance = UserCustom.objects.get(username = username, phonenumber = phonenumber, email = email)
#             instance.set_password(new_password)
#             instance.save()
#             return Response({'success':'password change success'})
#         except:
#             return Response({'error':'matching user not found'})