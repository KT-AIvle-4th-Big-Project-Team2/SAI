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
        
        col_data = ["점포_수","개업_점포_수","폐업_점포_수",
                    "프랜차이즈_점포_수","점포별_평균_매출_금액",
                    
                    #매출
                    "당월_매출_금액","주중_매출_금액","주말_매출_금액",
                    "월요일_매출_금액","화요일_매출_금액","수요일_매출_금액","목요일_매출_금액","금요일_매출_금액",
                    "토요일_매출_금액","일요일_매출_금액",
                    "시간대_00_06_매출_금액","시간대_06_11_매출_금액",
                    "시간대_11_14_매출_금액","시간대_14_17_매출_금액",
                    "시간대_17_21_매출_금액","시간대_21_24_매출_금액",
                    "남성_매출_금액","여성_매출_금액","연령대_10_매출_금액",
                    "연령대_20_매출_금액","연령대_30_매출_금액","연령대_40_매출_금액",
                    "연령대_50_매출_금액","연령대_60_이상_매출_금액",
                    
                    
                    #인구
                    #주거 인구
                    "총_상주인구_수","남성_상주인구_수","여성_상주인구_수",
                    "연령대_10_상주인구_수","연령대_20_상주인구_수","연령대_30_상주인구_수",
                    "연령대_40_상주인구_수","연령대_50_상주인구_수","연령대_60_이상_상주인구_수",
                    "남성연령대_10_상주인구_수","남성연령대_20_상주인구_수","남성연령대_30_상주인구_수",
                    "남성연령대_40_상주인구_수","남성연령대_50_상주인구_수","남성연령대_60_이상_상주인구_수",
                    "여성연령대_10_상주인구_수","여성연령대_20_상주인구_수","여성연령대_30_상주인구_수",
                    "여성연령대_40_상주인구_수","여성연령대_50_상주인구_수","여성연령대_60_이상_상주인구_수",
                    #유동인구
                    "총_유동인구_수","남성_유동인구_수","여성_유동인구_수",
                    "연령대_10_유동인구_수","연령대_20_유동인구_수","연령대_30_유동인구_수",
                    "연령대_40_유동인구_수","연령대_50_유동인구_수","연령대_60_이상_유동인구_수",
                    "시간대_00_06_유동인구_수","시간대_06_11_유동인구_수","시간대_11_14_유동인구_수",
                    "시간대_14_17_유동인구_수","시간대_17_21_유동인구_수","시간대_21_24_유동인구_수",

                    "월요일_유동인구_수","화요일_유동인구_수","수요일_유동인구_수","목요일_유동인구_수",
                    "금요일_유동인구_수","토요일_유동인구_수","일요일_유동인구_수",
                    
                    
                    #배후지
                    "관공서_수","은행_수","종합병원_수","일반_병원_수",
                    "유치원_수","초등학교_수","중학교_수","고등학교_수","대학교_수",
                    "백화점_수","슈퍼마켓_수" , "숙박_시설_수","공항_수","철도_역_수",
                    "버스_터미널_수","버스_정거장_수",
                    
                    #소비 트렌드
                    "식료품_지출_총금액","의류_신발_지출_총금액","생활용품_지출_총금액",
                    "의료비_지출_총금액","교통_지출_총금액","교육_지출_총금액","유흥_지출_총금액",
                    "여가_문화_지출_총금액","기타_지출_총금액","음식_지출_총금액",
                    
                    
                    ]
        
        
        queryset_dong_20233 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20232 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20231 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20224 = Dong_report_data.objects.filter(행정동_코드_명 = dong_name,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values(*col_data)
        
        #점포
        
        store_count = []
        
        #매출
        
        
        #인구
        
        
        #배후지
        
        
        #소비트렌드
        
        
        
        
        
        
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
        
        queryset_estimate = seoul_rent_db.objects.filter(dong_name=name_dong).values("area_name")
        
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
        
        seedmoney = 50000
        

        franchise_col = ["브랜드명","평균매출금액","가맹금액","교육금액","보증금액","기타금액","합계금액"]
        
        #queryset_franch1 = franchise_data.objects.filter(합계금액__lte = seedmoney).all()
        # 시드 머니에 임대료 +  보증금 (임대료 *10) 제외
        seedmoney = seedmoney - (rentcost*11)
        
        queryset_franch1 = franchise_data.objects.filter(중분류서비스 = "치킨",합계금액__lte = seedmoney).order_by('평균매출금액').values(*franchise_col)
        
        franchise_sort_data = queryset_franch1[::-1]
        #franchise_data[0]
        response_data= {
            "임대료" : rent_cost
        }
        
        fran_response_last =   [franchise_sort_data[0],franchise_sort_data[1],rent_cost]
        
        #franchise_sort_data[0]["브랜드명"]
        #franchise_sort_data[0]["평균매출금액"]
        #franchise_sort_data[0]["가맹금액"]
        #franchise_sort_data[0]["교육금액"]
        #franchise_sort_data[0]["보증금액"]
        #franchise_sort_data[0]["기타금액"]
        #franchise_sort_data[0]["합계금액"]
        
        
        return Response({"임대료" : rent_cost , "프랜차이즈 1 브랜드" : franchise_sort_data[0]["브랜드명"],
                         "프랜차이즈 1 평균매출금액" : franchise_sort_data[0]["평균매출금액"],"프랜차이즈 1 가맹금액" : franchise_sort_data[0]["가맹금액"],
                         "프랜차이즈 1 교육금액" : franchise_sort_data[0]["교육금액"],"프랜차이즈 1 보증금액" : franchise_sort_data[0]["보증금액"],
                         "프랜차이즈 1 기타금액" : franchise_sort_data[0]["기타금액"],"프랜차이즈 1 합계금액" : franchise_sort_data[0]["합계금액"],
                         "프랜차이즈 2 브랜드" : franchise_sort_data[1]["브랜드명"],
                         "프랜차이즈 2 평균매출금액" : franchise_sort_data[1]["평균매출금액"],"프랜차이즈 2 가맹금액" : franchise_sort_data[1]["가맹금액"],
                         "프랜차이즈 2 교육금액" : franchise_sort_data[1]["교육금액"],"프랜차이즈 2 보증금액" : franchise_sort_data[1]["보증금액"],
                         "프랜차이즈 2 기타금액" : franchise_sort_data[1]["기타금액"],"프랜차이즈 2 합계금액" : franchise_sort_data[1]["합계금액"],
                         
                         }, status=status.HTTP_200_OK)
        
        #return  Response({franchise_sort_data[1]["평균매출금액"]}) 
    
