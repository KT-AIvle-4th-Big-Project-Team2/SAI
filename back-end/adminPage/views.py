from django.shortcuts import render
from account.models import *
from board.models import *
from consultBoard.models import *
from faq.models import *
# from reviewBoard.models import *
from suggestions.models import *
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics


from urllib.parse import unquote



class UserList(APIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        username = self.request.data.pop('username')
        if not UserCustom.objects.get(username = username).is_superuser : return Response({'error':'not admin'}, status.HTTP_403_FORBIDDEN)
        
        
        if kwargs['function'] == 'list' and kwargs['first'] == 'none' and kwargs['second'] == 'none':
            queryset = UserCustom.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        
        elif kwargs['function'] == 'search':
            if kwargs['first'] == 'username':
                queryset = UserCustom.objects.filter( username = unquote(kwargs['second']))
                
            elif kwargs['first'] == 'name':
                queryset = UserCustom.objects.filter( name = unquote(kwargs['second']))
                
            elif kwargs['first'] == 'email':
                queryset = UserCustom.objects.filter( email = unquote(kwargs['second']))
                
            elif kwargs['first'] == 'phonenumber':
                queryset = UserCustom.objects.filter( phonenumber = unquote(kwargs['second']))
                
            elif kwargs['first'] == 'gender':
                queryset = UserCustom.objects.filter( gender = unquote(kwargs['second']))
            else:
                return Response({'error':'field does not exists'}, status.HTTP_404_NOT_FOUND)
                
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data, status.HTTP_200_OK)
        
        else:
            return Response({'error':'function does not exists'}, status.HTTP_404_NOT_FOUND)
    
    


class UserManager(APIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        key = self.request.data.pop('key')
        if not UserCustom.objects.get(username = key).is_superuser : return Response({'error':'no auth'}, status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data = self.request.data, partial = True)

        try:
            user = UserCustom.objects.get(user_id = kwargs['user_id'])
        except:
            raise ValidationError({'error':'username no match'}, status.HTTP_400_BAD_REQUEST)
        
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
            
            user.save()
            
            return Response({'success': "user update success"}, status.HTTP_200_OK)
        
        else:
            raise ValidationError({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, requset, *args, **kwargs):
        try:
            user_instance = UserCustom.objects.get(user_id = kwargs['user_id'])
        except:
            raise ValidationError({'error':'user_id no match'}, status.HTTP_400_BAD_REQUEST)
        
        user_instance.delete()
        return Response({'success':'user delete success'}, status.HTTP_200_OK)
    
    

class ManageBoard(APIView):
    
    def post(self, *args, kwargs):
        username = self.request.data.pop('username')
        if not UserCustom.objects.get(username = username).is_superuser : return Response({'error':'no auth'}, status.HTTP_403_FORBIDDEN)
        
        if kwargs['category'] == 'board':
            try:
                instance = Board.objects.get(board_id = kwargs['target'])
            except:
                raise ValidationError({'error' : 'no post found'}, status.HTTP_400_BAD_REQUEST)
            
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
        
    


class ManageComment(APIView):
    #permission_classes = (permissions.IsAdminUser,)
    
    def post(self, *args, kwargs):
        username = self.request.data.pop('username')
        if not UserCustom.objects.get(username = username).is_superuser : return Response({'error':'no auth'}, status.HTTP_403_FORBIDDEN)
        
        if kwargs['category'] == 'board':
            try:
                instance = Comments.objects.filter(comment_id = kwargs['comment_id'])
            except:
                raise ValidationError({'error' : 'no comment found'}, status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({'success':'post delete success'}, status.HTTP_200_OK)
        
        elif kwargs['category'] == 'consultboard':
            try:
                instance = CommentsConsult.objects.filter(comment_id = kwargs['comment_id'])
            except:
                raise ValidationError({'error' : 'no comment found'}, status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({'success':'comment delete success'}, status.HTTP_200_OK)
        
        else:
            raise ValidationError({'error' : 'no category match'}, status.HTTP_400_BAD_REQUEST)