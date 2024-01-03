# 시리얼라이저 안 쓰는 테스트 코드 사용시 
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .forms import signinForm

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import *
from .serializers import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# ... (your other imports)

class SignInView(generics.CreateAPIView):
    serializer_class = SignInSerializer
    
    def perform_create(self, serializer):
        new_user_data = serializer.validated_data
        username = new_user_data['name']

        if User.objects.filter(name=username).exists() or Admin.objects.filter(name=username).exists():
            raise ValidationError({'message': "That username is already used!"})
        
        serializer.save()

        return Response({'message': "User created successfully"}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('name')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

# ... (other views)



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
        
    
    
# # 제대로 된 로그인 시스템을 만들기 전 임시로 만든 비번 재확인 기능
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
    
    
    
    
    

# REST API 적용 전 테스트용 코드
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