from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse #http응답객체. HttpResponse는 클라이언트에게 200을 보내줌.
from .models import *
from .serializers import *

import json, requests, math
from time import sleep
from urllib.parse import unquote
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
# Create your views here.


class dong_report(APIView):
    
    def get(self, request):
        
        dong_name = "천호3동"
        business = "한식음식점"
        
        queryset_dong_20233 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values()
        queryset_dong_20232 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values()
        queryset_dong_20231 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values()
        queryset_dong_20224 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values()
        
        
        
        return Response(queryset_dong_20233, status=status.HTTP_200_OK)
        



class rent_cost(APIView):
    
    def get(self, request):
        #goo = unquote(self.kwargs['goo'])
        #dong = self.kwargs['dong'].upper()
        dong1 = "청운효자동" # null
        dong2 = "사직동" # one
        dong3 = "미아동" # two
        
        #business = self.kwargs['business'].upper()
        #funds = self.kwargs['seedMoney']
        
        
        #dong_name = seoul_rent_db.objects.all()

        # 임대료 데이터 초기 설정 
        rent_cost_last_data = 0
        
        queryset_estimate = seoul_rent_db.objects.filter(dong_name = dong3).values("area_name")
        
        # 행정동 입력 →  seoul_rent ( dong_name → 지명 확인) 

        vacancy_data = ["임대료","평균임대면적"]

        area_name = len(queryset_estimate)

        #임대료 데이터가 존재하거나 하나일 경우
        if len(queryset_estimate) == 1 :
            # temp_data = vacancyrate 상세지역
            temp_data = queryset_estimate[0]["area_name"]
            
            print(temp_data)
            
            # temp = "" 이면 임대료 정보 x
            if temp_data != "":
                rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data = rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
            else :
                rent_cost_last_data = -1
        
        # 임대료 데이터가 중복일 경우
        else :
            rent_cost_last_data = len(queryset_estimate) 
    
             
            for i in range(len(queryset_estimate) ):
                temp_data = queryset_estimate[i]["area_name"]
                rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data += rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
                print(rent_cost_last_data)

            rent_cost_last_data = rent_cost_last_data / len(queryset_estimate) 
                
        
        return Response(rent_cost_last_data, status=status.HTTP_200_OK)
        
# class rent_cost(APIView):
    
#     def get(self, request):
        
#         rent_cost_last_data = 0
        
#         queryset_estimate = seoul_rent_db.objects.filter(dong_name = dong3).values("area_name")
        
#         # 행정동 입력 →  seoul_rent ( dong_name → 지명 확인) 

#         vacancy_data = ["임대료","평균임대면적"]

#         area_name = len(queryset_estimate)

#         #임대료 데이터가 존재하거나 하나일 경우
#         if len(queryset_estimate) == 1 :
#             # temp_data = vacancyrate 상세지역
#             temp_data = queryset_estimate[0]["area_name"]
            
#             print(temp_data)
            
#             # temp = "" 이면 임대료 정보 x
#             if temp_data != "":
#                 rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
#                 rent_cost_last_data = rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
#             else :
#                 rent_cost_last_data = -1
        
#         # 임대료 데이터가 중복일 경우
#         else :
#             rent_cost_last_data = len(queryset_estimate) 
    
             
#             for i in range(len(queryset_estimate) ):
#                 temp_data = queryset_estimate[i]["area_name"]
#                 rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
#                 rent_cost_last_data += rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
#                 print(rent_cost_last_data)

#             rent_cost_last_data = rent_cost_last_data / len(queryset_estimate) 
                
        
#         return Response(rent_cost_last_data, status=status.HTTP_200_OK)
                
def rent_cost_data(name_dong):
        rent_cost_last_data =1
        
        queryset_estimate = seoul_rent_db.objects.filter(name_dong).values("area_name")
        
        vacancy_data = ["임대료","평균임대면적"]

        area_name = len(queryset_estimate)

        #임대료 데이터가 존재하거나 하나일 경우
        if len(queryset_estimate) == 1 :
            # temp_data = vacancyrate 상세지역
            temp_data = queryset_estimate[0]["area_name"]
            
            # temp = "" 이면 임대료 정보 x
            if temp_data != "":
                rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data = rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
            else :
                rent_cost_last_data = -1
        
        # 임대료 데이터가 중복일 경우
        else :
            rent_cost_last_data = len(queryset_estimate) 
    
             
            for i in range(len(queryset_estimate) ):
                temp_data = queryset_estimate[i]["area_name"]
                rent_cost = vacancyrate_db.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data += rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
                print(rent_cost_last_data)

            rent_cost_last_data = rent_cost_last_data / len(queryset_estimate) 
        
        return rent_cost_last_data
           
        
# 프랜차이즈 작업 더 필요
class franchisedata(APIView):
    
    
    def get(self, request):
        
        dongname = "미아동"
        Sectors = "치킨"
        rentcost = rent_cost_data(dongname)
        
        seedmoney = 5000
        

        
        queryset_franch1 = franchise_data.objects.filter(합계금액__lte = seedmoney).all
        queryset_franch2 = franchise_data.objects.filter(중분류서비스 = "치킨").values()
        
        
        #for i in range(len(test_data)):
            
        return Response(queryset_franch2, status=status.HTTP_200_OK)


    
