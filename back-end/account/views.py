from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from .models import UserCustom
from .serializers import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from urllib.parse import unquote


# 계정 및 로그인 관련 기능

# 회원가입 기능 View
class SignInView(APIView):
    serializer_class = SignInSerializer
    
    def post(self, request):

        serializer = self.serializer_class(data = self.request.data)
        
        # 유저 테이블인 UserCustom ModelSerializer로 유효성 검사
        if serializer.is_valid(): 
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            password = serializer.validated_data['password'] 
            email = serializer.validated_data['email']
            phonenumber = serializer.validated_data['phonenumber']
            age = serializer.validated_data['age']
            gender = serializer.validated_data['gender']
            
            # 유효성 검사 실패시 에러 내용과 400을 상태로 보냄
        else:
            raise ValidationError({'error':serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        # 유효성 검사 성공시 create_user를 사용해 password 암호화 및 유저를 DB에 추가
        user = UserCustom.objects.create_user(username = username, password = password, name = name, email = email, 
                                        phonenumber = phonenumber, age = age, gender = gender)
        user.save()
        return Response({'success': "User created successfully"})


# 로그인 기능 View
class LoginView(APIView):
    serializer_class = LoginSerializer
    

    def post(self, request, format = None):
        
        # 유저의 입력 값을 serializer에 입력
        serialized = self.serializer_class(data = request.data)
        
        # serialzier 입력 유효성검사
        if serialized.is_valid():
            email = serialized.validated_data['email']
            password = serialized.validated_data['password']
            
            # 유효한 email로 username 조회
            username = UserCustom.objects.get(email = email).username
            
            # authenticate로 username과 암호화 된 비밀번호 일치 확인
            user_info = authenticate(username = username, password=password)
            
            # authenticate 실패, 메시지 반환
            if user_info != None:
                return Response({'success' : 'login successful', 'username' : username}, status=status.HTTP_200_OK)
            else:
                  return Response({'error' : 'wrong user info'})
        else:
            return Response({'error':'input value error'})


# 로그아웃 기능
class LogoutView(APIView):
    def post(self, request, format = None):
        
        try:
            return Response({'success':'logout success'})
        except:
            return Response({'error':'logout failed'})


# 유저정보 수정
class UpdateUserInfo(generics.GenericAPIView):
    serializer_class = UpdateUserSerializer

    def patch(self, request, *args, **kwargs):
        
        username = unquote(kwargs['username'])
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


# password 찾기
class findPWView(generics.GenericAPIView):
    serializer_class =FindPwSerialzer
    
    # 입력 데이터 serializer 입력
    def post(self, request):
        serialized = self.serializer_class(data =request.data)
        
        # 입력 데이터 유효성 확인
        if serialized.is_valid():
            
            # 입력 id, email로 계정확인
            try: 
                UserCustom.objects.get(username = serialized.validated_data['username'], email = serialized.validated_data['email'])
                
                # 계정확인 시 password 초기화 페이지 링크 전송
                return Response({'matchig user found email sent'}, status.HTTP_200_OK)
            except:
                
                # 유저 검색 실패 시 에러 메시지 전송
                return Response(["no matching user found"], status.HTTP_404_NOT_FOUND)
        else:
            # 데이터 유효성 검사 실패 시 에러 메시지 전송
            return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)


# password 확인
class CheckPWView(APIView):
    
    def post(self, request):
        
        # serializer 입력
        serialized = PasswordCheckSerializer(data = request.data)
        
        if serialized.is_valid():
            try:
                # username으로 DB에서 유저 정보 조회
                instance = UserCustom.objects.get(username = serialized.validated_data["username"])
            except:
                # 유저 정보 조회 실패, 에러 메시지 반환
                return Response({"error":"user info error"})
            
            # 입력한 비밀번호와 암호화된 비밀번호 비교 검사
            if check_password(serialized.validated_data['password'], instance.password ):
                
                # 일치 확인, 메시지 전송
                return Response({'success':'password check success'}, status.HTTP_200_OK)
            else:
                # 불일치 확인, 메시지 전송
                return Response({'error':'password is wrong'}, status.HTTP_403_FORBIDDEN)
        else:
            # 입력 데이터 유효성 검사 실패, 메시지 전송
            return Response({"error":"user info error"}, status.HTTP_400_BAD_REQUEST)


# 유저 정보 조회
class GetUserView(APIView):
    serializer_class = GetUserData 

    def get(self, *args, **kwargs):
        
        try: # 입력 username으로 유저 정보 조회
            user_data = UserCustom.objects.get(username = unquote(kwargs['username']))
            
            # 유저 정보 확인, 유저 데이터 전송
            if user_data:
                serializer = self.serializer_class(user_data)
                return Response(serializer.data)
            
            # 유저 정보 확인 실패, 메시지 전송
            else:
                return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
            
            # 입력 데이터 유효성 실패, 메시지 전송
        except:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)
        


# 유저 계정 삭제
class DeleteAccountView(APIView):
    def delete(self, *args, **kwargs):
        
        # username 입력 조회
        try:
            userinfo = UserCustom.objects.get(username = unquote(kwargs["username"]))
                
                # 조회 성공, 유저 삭제
            userinfo.delete()           
            return Response({f"user deleted success"}, status.HTTP_200_OK)
        except:
            # 조회 실패, 실패 메시지 전송
            return Response({"no username matched"}, status=status.HTTP_400_BAD_REQUEST)