from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import LogInfo, UserCustom
from .serializers import *

from account.customlibs.checkLogin import *

# from pycaret.regression import *


# 23년 3분기 예측
class dong_predict(APIView):
    def get(self, request, *args, **kargs):
        # querry = 
        
        final_model = finalize_model(blender_5)
        prediction = predict_model(final_model, data = test)
        
        
        return Response({"test":"testing"}, status=status.HTTP_200_OK)

# 23년 3분기 추정
class dong_estimate(APIView):
    def get(self, request, *args, **kargs):
        
        return Response({"test":"testing"}, status=status.HTTP_200_OK)
    
# 23년 3분기 예측
class market_predict(APIView):
    def get(self, request, *args, **kargs):
        
        return Response({"test":"testing"}, status=status.HTTP_200_OK)
 
# 23년 3분기 추정    
class market_estimate(APIView):
    def get(self, request, *args, **kargs):
        
        return Response({"test":"testing"}, status=status.HTTP_200_OK)
    
    