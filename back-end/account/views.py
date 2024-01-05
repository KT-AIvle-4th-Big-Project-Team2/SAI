# 시리얼라이저 안 쓰는 테스트 코드 사용시 
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .forms import signinForm

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import LogInfo, UserCustom
from .serializers import *

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from account.customlibs.checkLogin import *



@method_decorator(ensure_csrf_cookie, name='dispatch') # 바로 아래의 View를 호출하면 CSRF 토큰을 전달하도록 설정        
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)
    
    
    def get(self, request, format = None):
        return Response({'success' : 'CSRF Cookie set'})

class CheckAuthenticatedView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format = None):
        try:
            isAuthenticated = request.user.is_authenticated
            
            if isAuthenticated:
                return Response({'isAuthenticated':'sucess'})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error': 'Something went wrong during checking authentication status'})


#@method_decorator(csrf_protect, name='dispatch')
class SignInView(generics.CreateAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = SignInSerializer
    
    def perform_create(self, serializer):
        try:
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']
            phonenumber = serializer.validated_data['phonenumber']
            age = serializer.validated_data['age']
            gender = serializer.validated_data['gender']
        except:
            raise ValidationError({'error':'input value error'})
        #if UserCustom.objects.filter(username=username).exists() or Admin.objects.filter(name=username).exists(): # Admin 테이블을 따로 사용할 경우 활성화
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error':'username already exists'})
        else:
            user = UserCustom.objects.create_user(username = username, password = password, email = email, 
                                            phonenumber = phonenumber, age = age, gender = gender)
            user.save()
            return Response({'success': "User created successfully"})

# @method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    #permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    
    def post(self, request, format = None):
        serialized = self.serializer_class(data = request.data)
        if serialized.is_valid():
            username = serialized.validated_data['username']
            password = serialized.validated_data['password']
            
            user_info = authenticate(username=username, password=password)
            if user_info != None:
                auth.login(request, user_info)
                return Response({'success' : 'login successful'}, status=status.HTTP_202_ACCEPTED)
            else:
                  return Response({'error' : 'wrong user info'})
        else:
            return Response({'error':'input value error'})


#@method_decorator(csrf_protect, name='dispatch')
class UpdatePWView(generics.UpdateAPIView):
    serializer_class = UpdatePWSerializer
    
    def patch(self, request, *args, **kwargs):
        
        key = request.data.get('key')
        
        if not LoginCheck(key):  raise ValidationError({"error":"user info error"})
        instance = UserCustom.objects.get(username = key)
        request.data.pop('key', None)
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            instance.set_password(serializer.validated_data['password'])
            print(1)
            instance.save()
            return Response({'success':'pw update success'})
        else:
            return Response({'error':'input error'})
        
        
class LogoutView(APIView):
    def post(self, request, format = None):
        try:
            auth.logout(request)
            return Response({'success':'logout success'})
        except:
            return Response({'error':'logout failed'})



#@method_decorator(csrf_protect, name='dispatch')
# class LogoutView(APIView):
#     def post(self, request, format = None):
#         try:
#             #auth.logout(request)
#             key = request.data.get('key')
#             if not LoginFalse(key):  raise ValidationError({"error":"user info error"})
#             return Response({'success':'logout success'})
#         except:
#             return Response({'error':'logout failed'})
        

class GetUserView(APIView):
    serializer_class = GetUserData  # 수정

    def post(self, request, format=None):
        username = request.data.get("username")
        
        if username:
            user_data = UserCustom.objects.filter(username=username).first()
            if user_data:
                serializer = self.serializer_class(user_data)
                return Response(serializer.data)
            else:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)
    
class CheckPWView(APIView):
    serializer_class = PasswordCheckSerializer
    def post(self, request):
        key = request.data.get('key')
        if not LoginCheck(key):  raise ValidationError({"error":"user info error"})
        request.data.pop('key', None)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                instance = UserCustom.objects.get(username = key)
            except:
                return Response({"error":"user info error"})
            
            if check_password(serializer.validated_data['password'], instance.password ):
                return Response({'success':'login success'})
            else:
                return Response({'error':'password is wrong'})
        else:
            return Response({"error":"user info error"})
        

class DeleteAccountView(APIView):
    serializer_class = PasswordCheckSerializer
    def delete(self, request):
        key = request.data.get('key')
        if not LoginCheck(key):  raise ValidationError({"error":"user info error"})
        request.data.pop('key', None)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                instance = UserCustom.objects.get(username = key)
            except:
                return Response({"error":"user doesn't exists error"})
            
            if check_password(serializer.validated_data['password'], instance.password ):
                LoginFalse(key)
                instance.delete()
                return Response({"success":"user deleted"})
            else:
                return Response({'error':'password is wrong'})
        else:
            return Response({"error":"user info error"})
        
class FindIDView(APIView):
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
            instance = UserCustom.objects.get(username = username, phonenumber = phonenumber, email = email)
            instance.set_password(password)
            instance.save()
            return Response({'success':'password change success'})
        except:
            return Response({'error':'matching user not found'})
        
class SendPing(APIView):
    serializer_class = FindIDOutputSerializer
    def post(self, request):
        key = request.data.get("key")
        if not LoginCheck(key):  raise ValidationError({"error":"user info error"})
        else:
            return Response({'success' : 'ping success'})
        

     
     
     
     
     
# SESSION 사용 시 이용할 코드
     
     
# CSRF 토큰 발급
# @method_decorator(ensure_csrf_cookie, name='dispatch') # 바로 아래의 View를 호출하면 CSRF 토큰을 전달하도록 설정    
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, format = None):
#         return Response({'success' : 'CSRF Cookie set'})

#@method_decorator(csrf_protect, name='dispatch')
# SESSOIN ID 검사
# class CheckAuthenticatedView(APIView):
#     def get(self, request, format = None):
#         try:
#             isAuthenticated = request.user.is_authenticated
            
#             if isAuthenticated:
#                 return Response({'isAuthenticated':'sucess'})
#             else:
#                 return Response({'isAuthenticated':'error'})
#         except:
#             return Response({'error': 'Something went wrong during checking authentication status'})


# SESSION ID 사용 시 활성화 할 LOGIN
# def post(self, request, format = None):
#     print(request.data)
#     serializer = self.serializer_class(data=request.data)
#     print(serializer.is_valid())
#     if serializer.is_valid():
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#         user = auth.authenticate(username = username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return Response({'success' : 'user login successs'})
#         else:
#             return Response({'error':'user login failed'})
#     else:
#         return Response({"error":"login data error"})    

#@method_decorator(csrf_protect, name='dispatch')
# class UpdateUserView(generics.UpdateAPIView):
#     queryset = UserCustom.objects.all()
#     serializer_class = UpdateUserSerializer

#     def patch(self, request, *args, **kwargs):
#         user = self.get_object()  # 뷰의 queryset에서 사용자를 가져옵니다.
#         serializer = self.serializer_class(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# SESSION ID 전용        
#@method_decorator(csrf_protect, name='dispatch')
# class GetUserView(APIView):
#     serializer_class = GetUserData
#     def get(self, request, format = None):
#         user = self.request.user
#         user_data = UserCustom.objects.filter(username = user).first()
#         print(user_data)
#         serializer = self.serializer_class(user_data)
#         return Response(serializer.data)
     
     
     
     
     
     
     
     
     
     
     
# 제대로 된 로그인 시스템을 만들기 전 임시로 만든 기능       
# class SignInView(generics.CreateAPIView):
#     serializer_class = SignInSerializer    
#     def perform_create(self, serializer):
#         new_user_data = serializer.validated_data
#         username = new_user_data['name']
#         if User.objects.filter(name=username).exists() or Admin.objects.filter(name=username).exists():
#             raise ValidationError({'message': "That username is already used!"})
#         serializer.save()
#         return Response({'message': "User created successfully"}, status=status.HTTP_201_CREATED)
    
# class LoginView(APIView):
#     serializers = LoginSerializer
#     def post(self, request):
#         serializer = self.serializers(data=request.data)
#         if serializer.is_valid():
#             inputs = serializer.validated_data
#             username = inputs['name']
#             password = inputs['password']
#             if User.objects.filter(name = username).exists():
#                 print("id matched")
#                 potentialUserRow = User.objects.filter(name = username).first()
#                 if password == potentialUserRow.password:
#                     print("password matched")
#                     return Response({'message': "user login successful"}, status=status.HTTP_200_OK,)
#                 else: return Response({'message': "password wrong"}, status.HTTP_401_UNAUTHORIZED,)
#             elif Admin.objects.filter(name = username).exists():
#                 print("Admin Id matched!")
#                 potentialAdminRow = Admin.objects.filter(name = username).first()
#                 if password == potentialAdminRow.password:
#                     print("password matched!")
#                     return Response({'message': "admin login successful"}, status=status.HTTP_200_OK,)
#                 else: return Response({'message': "password wrong"}, status.HTTP_401_UNAUTHORIZED,)
#             else: return Response({'message': "id wrong"}, status.HTTP_401_UNAUTHORIZED,)
#         else: return Response(status.HTTP_400_BAD_REQUEST)
        
# class FindIDView(APIView):
#     queryset = User.objects.all()
#     def post(self, request):
#         self.queryset
#         serializer_data = FindIDInputSerializer(data=request.data)
#         if serializer_data.is_valid():
#             inputs = serializer_data.validated_data
#             email = inputs['email']
#             phonenumber = inputs['phonenumber']
#             gender = inputs['gender']
#             try:
#                 matchingUser = User.objects.filter(email = email, phonenumber = phonenumber, gender =gender)
#                 matchingUserDatas = FindIDOutputSerializer(matchingUser, many = True)
#                 return Response(matchingUserDatas.data, status=status.HTTP_200_OK)
#             except:
#                 raise ValidationError({'message':'matching user not found!'})
#         return  Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class FindPasswordView(APIView):    
#     def post(self, request):
#         serializer_data = FindPasswordInputSerializer(data=request.data)
#         if serializer_data.is_valid():
#             inputs = serializer_data.validated_data
#             name = inputs['name']
#             email = inputs['email']
#             phonenumber = inputs['phonenumber']
#             gender = inputs['gender']
#             try:
#                 matchingUser = User.objects.filter(name = name, email = email, phonenumber = phonenumber, gender =gender)
#                 matchingUserDatas = FindPasswordOutputSerializer(matchingUser, many = True)
#                 return Response(matchingUserDatas.data, status=status.HTTP_200_OK)
#             except:
#                 raise ValidationError({'message':'matching user not found!'})
#         return  Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UpdateUserView(generics.UpdateAPIView):
#     serializer_class = UpdateUserSerializer
#     queryset = User.objects.all()
#     lookup_field = 'name'
#     def get_object(self):
#         # Use the provided lookup_field to filter the queryset
#         filter_kwargs = {self.lookup_field: self.request.data.get(self.lookup_field)}
#         target = self.get_queryset().filter(**filter_kwargs).first()
#         return target
    
#     def perform_update(self, serializer):
#         instance = self.get_object()
#         #instance = self.queryset.filter(name = serializer.validated_data['name'])
#         instance.password = serializer.validated_data['password']
#         instance.email = serializer.validated_data['email']
#         instance.phonenumber = serializer.validated_data['phonenumber']
#         instance.age = serializer.validated_data['age']
#         instance.gender = serializer.validated_data['gender']
#         instance.save()
        
# class DeleteUserView(APIView):
#     serializer_class = DeleteUserSerializer
#     def post(self, request):
#         serializerd_data = self.serializer_class(data = request.data)
#         if serializerd_data.is_valid():
#             targetName = serializerd_data.validated_data.get('name', None)
#         print(targetName)
#         print(type(targetName))
#         self.delete(request, targetName = targetName)
#         return Response({'message': "User data is deleted!"}, status=status.HTTP_200_OK,)
    
#     def delete(self, request, targetName, *args, **kwargs):
#         target = User.objects.filter(name = targetName).first()
#         target.delete()

# class PWCheckView(APIView):    
#     def post(self, request):
#         serializer_data = PasswordCheckSerializer(data=request.data)
#         if serializer_data.is_valid():
#             inputs = serializer_data.validated_data
#             name = inputs['name']
#             password = inputs['password']
#             if User.objects.filter(name = name, password = password).exists():
#                 return Response({'message': "Password check pass!"}, status=status.HTTP_200_OK,)
#             else:
#                 raise ValidationError({'message':'password doesnt match!'})
#         return  Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

# # REST API 적용 전 테스트용 코드
# def testing(request):
#     return HttpResponse("account app is running fine!")

# def signIn(request):
    
#     print(request.method)
#     print("get: ", request.GET)
#     print("get: ", request.POST)
    
#     if request.method == 'POST':
#         form = signinForm(request.POST)
#         if form.is_valid():
#             print("input valid")
#             form.save()
#             return redirect('new_account_success/')
#         else:
#             print("input not valid")

#     return render(request, "account/signin.html")

# def login(request):
    
#     print(request.method)
#     print("get: ", request.GET)
#     print("get: ", request.POST)
    
#     if request.method == 'POST':
#         if User.objects.filter(name = request.POST.get('name')).exists():
#             print("Matching username found!")
#             potentialUser = User.objects.filter(name = request.POST.get('name')).first()
#             if potentialUser.password == request.POST.get('password'):
#                 print("Password's also matchs!")
#                 return HttpResponse("Login successful!")
#             else:
#                 return HttpResponse("Password is wrong! Your device will detonate in 10 seconds!")
#         else:
#             if Admin.objects.filter(name = request.POST.get('name')).exists():
#                 print("Matching admin name found!")
                
#                 potentialUser = Admin.objects.filter(name = request.POST.get('name')).first()
#                 if potentialUser.password == request.POST.get('password'):
#                     print("Admin password's also matchs!")
#                     return HttpResponse("Admin login successful!")
#                 else:
#                     return HttpResponse("Password is wrong!\n Your device will detonate in 10 seconds!")
#             else:
#                 return HttpResponse("Wrong ID!")
            

#     return render(request, "account/login.html")

# def signinSuccess(request):
    
#     return HttpResponse("sign in successful!")