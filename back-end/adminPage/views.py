from account.models import *
from board.models import *
from consultBoard.models import *
from faq.models import *
from suggestions.models import *
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from urllib.parse import unquote


# 관리자가 사이트 운영 시 필요한 기능 


# 유저 정보 조회
class UserList(APIView):
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        
        # function 값으로 기능 선택
        
        # function이 list, 유저 전체 조회
        if kwargs['function'] == 'list' and kwargs['first'] == 'none' and kwargs['second'] == 'none':
            queryset = UserCustom.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        
        # function이 search, 유저 검색
        elif kwargs['function'] == 'search':
            
            # first 값으로 검색 대상 선택
            
            # first가 username, second의 데이터로 검색
            if kwargs['first'] == 'username':
                queryset = UserCustom.objects.filter( username = unquote(kwargs['second']))
                
            # first가 name, second의 데이터로 검색
            elif kwargs['first'] == 'name':
                queryset = UserCustom.objects.filter( name = unquote(kwargs['second']))
                
            # first가 email, second의 데이터로 검색
            elif kwargs['first'] == 'email':
                queryset = UserCustom.objects.filter( email = unquote(kwargs['second']))
                
            # first가 phonenumber, second의 데이터로 검색
            elif kwargs['first'] == 'phonenumber':
                queryset = UserCustom.objects.filter( phonenumber = unquote(kwargs['second']))
                
            # first가 gender, second의 데이터로 검색
            elif kwargs['first'] == 'gender':
                queryset = UserCustom.objects.filter( gender = unquote(kwargs['second']))
            else:
                
                # first 해당 없음. 오류 메시지 반환
                return Response({'error':'field does not exists'}, status.HTTP_404_NOT_FOUND)
                
            # 출력 데이터 직렬화
            serializer = self.serializer_class(queryset, many=True)
            
            # 출력 데이터 전송
            return Response(serializer.data, status.HTTP_200_OK)
        
        # 일치 조건 없음, 오류 메시지 반환
        else:
            return Response({'error':'function does not exists'}, status.HTTP_404_NOT_FOUND)
    
    


# 유저 정보 관리
class UserManager(APIView):
    serializer_class = UserSerializer
    
    # 유저 정보 수정
    def patch(self, request, *args, **kwargs):
        
        # 입력 데이터 serializer 입력
        serializer = self.serializer_class(data = self.request.data, partial = True)

        try: # 유저 구분 id로 검색
            user = UserCustom.objects.get(user_id = kwargs['user_id'])
        except:
            raise ValidationError({'error':'username no match'}, status.HTTP_400_BAD_REQUEST)
        
        # 입력 데이터 유효시, 유저에 새 데이터 입력
        if serializer.is_valid():
            if 'username' in serializer.validated_data:
                user.username = serializer.validated_data['username']
            if 'name' in serializer.validated_data:
                user.name = serializer.validated_data['name']
            if 'password' in serializer.validated_data:
                user.set_password(serializer.validated_data['password'])
            if 'email' in serializer.validated_data:
                user.email = serializer.validated_data['email']
            if 'phonenumber' in serializer.validated_data:
                user.phonenumber = serializer.validated_data['phonenumber']
            if 'age' in serializer.validated_data:
                user.age = serializer.validated_data['age']
            if 'gender' in serializer.validated_data:
                user.gender = serializer.validated_data['gender']
            
            # 입력 내용 저장 및 응답 전송
            user.save()
            return Response({'success': "user update success"}, status.HTTP_200_OK)
        
        # 입력 데이터 유효성 검사 실패, 응답 전송
        else:
            raise ValidationError({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)    
    
    # 유저 삭제
    def delete(self, requset, *args, **kwargs):
        
        # 유저 구분 id로 대상 유저 조회
        try:
            user_instance = UserCustom.objects.get(user_id = kwargs['user_id'])
        except:
            # 조회 실패, 응답 전송
            raise ValidationError({'error':'user_id no match'}, status.HTTP_400_BAD_REQUEST)
        
        # 조회 성공, 삭제 및 응답 전송
        user_instance.delete()
        return Response({'success':'user delete success'}, status.HTTP_200_OK)
    
    


# 게시판 관리
class ManageBoard(APIView):
    
    # 작성자 확인 없이 게시글 삭제
    def delete(self, *args, kwargs):
        
        # 게시판 선택
        if kwargs['category'] == 'board':
            try:
                # 선택 게시물 조회
                instance = Board.objects.get(board_id = kwargs['target'])
            except:
                # 조회 실패, response 전송
                raise ValidationError({'error' : 'no post found'}, status.HTTP_400_BAD_REQUEST)
            
            # 조회 성공, 게시물 삭제
            instance.delete()
            return Response({'success':'post delete success'}, status.HTTP_200_OK)
        
        elif kwargs['category'] == 'consultboard':
            try:
                instance = Board.objects.get(board_id = unquote(kwargs['target']))
            except:
                raise ValidationError({'error' : 'no post found'}, status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({'success':'post delete success'}, status.HTTP_200_OK)
        
        elif kwargs['category'] == 'suggestions':
            try:
                instance = Board.objects.get(board_id = unquote(kwargs['target']))
            except:
                raise ValidationError({'error' : 'no post found'}, status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({'success':'post delete success'}, status.HTTP_200_OK)
        
        else:
            raise ValidationError({'error' : 'no category match'}, status.HTTP_400_BAD_REQUEST)
        
    

# 댓글 관리
# 작성자 검사 없이 댓글 삭제 기능
class ManageComment(APIView):
    
    def delete(self, *args, kwargs):
        
        # 게시판 선택
        if kwargs['category'] == 'board':
            try:
                # 댓글 조회
                instance = Comments.objects.get(comment_id = kwargs['comment_id'])
            except:
                # 조회 실패, response 전송
                raise ValidationError({'error' : 'no comment found'}, status.HTTP_400_BAD_REQUEST)
            
            # 조회 성공, 댓글 삭제 및 response 전송
            instance.delete()
            return Response({'success':'post delete success'}, status.HTTP_200_OK)
        
        elif kwargs['category'] == 'consultboard':
            try:
                instance = CommentsConsult.objects.get(comment_id = kwargs['comment_id'])
            except:
                raise ValidationError({'error' : 'no comment found'}, status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({'success':'comment delete success'}, status.HTTP_200_OK)
        
        else:
            raise ValidationError({'error' : 'no category match'}, status.HTTP_400_BAD_REQUEST)