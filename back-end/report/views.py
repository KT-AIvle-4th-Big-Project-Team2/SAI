from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse #http응답객체. HttpResponse는 클라이언트에게 200을 보내줌.
from .models import *
from .serializers import *
import re
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
        
        dong = "대조동"
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
        
        
        queryset_dong_20233 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20232 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20231 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20224 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20223 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20223 ,서비스_업종_코드_명 = business).values(*col_data)
        
        #1. 종합의견

        # 동 순위 계산
        queryset_dong_goo = SeoulRent.objects.filter(dong_name = dong).values("시군구명")
        queryset_dong_list = SeoulRent.objects.filter(시군구명 = queryset_dong_goo[0]["시군구명"]).values("dong_name")
        
        #return Response(queryset_dong_list)
        
        dong_count= len(queryset_dong_list)

        dong_names = [entry["dong_name"] for entry in queryset_dong_list]

        # 점포 매출액 유동인구
        dong_col = ["행정동_코드_명","점포_수","당월_매출_금액","총_유동인구_수"]
        dong_rank = []
        for i in dong_names :
            queryset_dong_data = DongSortedDbFin.objects.filter(행정동_코드_명 = i,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*dong_col)
            dong_rank.append(queryset_dong_data)

        # 빈리스트 제거
        dong_rank = [entry for entry in dong_rank if entry]
        
        
        #dong rank 데이터
        dong_rank_data = []

        sorted_data = sorted(dong_rank, key=lambda x: x[0]["점포_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        
        

        sorted_data = sorted(dong_rank, key=lambda x: x[0]["당월_매출_금액"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["총_유동인구_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        

        #전분기
        Quarterly_sales = int((queryset_dong_20233[0]["당월_매출_금액"] - queryset_dong_20232[0]["당월_매출_금액"])//10000)

        #전년도 분기 대비
        Sales_compared_to_the_same_quarter_last_year = int((queryset_dong_20233[0]["당월_매출_금액"] - queryset_dong_20223[0]["당월_매출_금액"])//10000)

        
        #종합 의견

        general_opinion = [Quarterly_sales,Sales_compared_to_the_same_quarter_last_year]
        #general_opinion = [data]


        #1-1 best 매출
        #성별
        gender_max = "남성" if queryset_dong_20233[0]["남성_매출_금액"] > queryset_dong_20233[0]["여성_매출_금액"] else "여성"

        # 연령대 중 가장 매출이 많은 것 찾기
        age_groups = ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"]
        age_max = max(age_groups, key=lambda x: queryset_dong_20233[0][f"{x}_매출_금액"])

        # 요일 중 가장 매출이 많은 것 찾기
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        day_max = max(days, key=lambda x: queryset_dong_20233[0][f"{x}_매출_금액"])
        total_sales = sum(queryset_dong_20233[0][f"{day}_매출_금액"] for day in ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])
        
        dat_percentages = round((queryset_dong_20233[0][f"{day_max}_매출_금액"] /total_sales *100),1)

        # 시간대 중 가장 매출이 많은 것 찾기
        time_ranges = ["시간대_00_06", "시간대_06_11", "시간대_11_14", "시간대_14_17", "시간대_17_21", "시간대_21_24"]
        time_max = max(time_ranges, key=lambda x: queryset_dong_20233[0][f"{x}_매출_금액"])


        best_gender_age_group = gender_max +"/" + re.sub("[^0-9]", "", age_max) +"대"
        best_sales_day = day_max+f"({dat_percentages}%)"
        best_sales_time = re.sub("[^0-9]", "", time_max)
        best_sales_time = best_sales_time[:2] + "~" + best_sales_time[2:] + "시"

        sales_data = [best_gender_age_group , best_sales_day , best_sales_time  ]

        #유동인구
        
        gender_max = "남성" if queryset_dong_20233[0]["남성_유동인구_수"] > queryset_dong_20233[0]["여성_유동인구_수"] else "여성"

        # 연령대 중 가장 인구이 많은 것 찾기
        age_groups = ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"]
        age_max = max(age_groups, key=lambda x: queryset_dong_20233[0][f"{x}_유동인구_수"])
        total_age_population = sum(queryset_dong_20233[0][f"{age}_유동인구_수"] for age in ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"])
        age_percentages = round((queryset_dong_20233[0][f"{age_max}_유동인구_수"] /total_age_population *100),1)

        # 요일 중 가장 인구이 많은 것 찾기
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        day_max = max(days, key=lambda x: queryset_dong_20233[0][f"{x}_유동인구_수"])
        total_population = sum(queryset_dong_20233[0][f"{day}_유동인구_수"] for day in ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])
        
        dat_percentages = round((queryset_dong_20233[0][f"{day_max}_유동인구_수"] /total_population *100),1)

        # 시간대 중 가장 매출이 많은 것 찾기
        time_ranges = ["시간대_00_06", "시간대_06_11", "시간대_11_14", "시간대_14_17", "시간대_17_21", "시간대_21_24"]
        time_max = max(time_ranges, key=lambda x: queryset_dong_20233[0][f"{x}_유동인구_수"])

        best_population_age_group =  re.sub("[^0-9]", "", age_max) +"대"+f"({age_percentages}%)"
        best_population_day = day_max+f"({dat_percentages}%)"
        best_population_time = re.sub("[^0-9]", "", time_max)
        best_population_time = best_population_time[:2] + "~" + best_population_time[2:] + "시"


        #유동인구
        floating_population = [gender_max , best_population_age_group ,best_population_day , best_population_time  ]



        
        #2.점포
        
        # 전년 동분기 대비
        Compared_to_the_same_quarter_last_year = queryset_dong_20233[0]["점포_수"] - queryset_dong_20223[0]["점포_수"]
        # 전분기 대비
        compared_to_the_previous_quarter = queryset_dong_20233[0]["점포_수"] - queryset_dong_20232[0]["점포_수"]
        
        if Compared_to_the_same_quarter_last_year > 0:
            status_of_business_districts = "증가"
            business_districts = "발달"
        else : 
            status_of_business_districts = "감소"
            business_districts = "쇠퇴"
            
        
        store_count = {
            "20223store_count" : queryset_dong_20223[0]["점포_수"],
            "20224store_count" : queryset_dong_20224[0]["점포_수"],
            "20231store_count" : queryset_dong_20231[0]["점포_수"],
            "20232store_count" : queryset_dong_20232[0]["점포_수"],
            "20233store_count" : queryset_dong_20233[0]["점포_수"],
            #전년 동분기 수치
            "csql1" : Compared_to_the_same_quarter_last_year,
            # 전 분기 수치
            "cpq1" :   compared_to_the_previous_quarter,
            # 안내 텍스트
            "sbd1" : status_of_business_districts,
            "bd1" : business_districts
        }
        
        # 개업 점포수 
        op_Compared_to_the_same_quarter_last_year =  queryset_dong_20233[0]["개업_점포_수"] -  queryset_dong_20223[0]["개업_점포_수"]
        op_compared_to_the_previous_quarter = queryset_dong_20233[0]["개업_점포_수"] -  queryset_dong_20232[0]["개업_점포_수"]
        if op_Compared_to_the_same_quarter_last_year > 0:
            op_status_of_business_districts = "증가"
            op_business_districts = "활발하"
        else : 
            op_status_of_business_districts = "감소"
            op_business_districts = "침체되"
            
        open_shop = {
            "20223openstore" : queryset_dong_20223[0]["개업_점포_수"],
            "20224openstore" : queryset_dong_20224[0]["개업_점포_수"],
            "20231openstore" : queryset_dong_20231[0]["개업_점포_수"],
            "20232openstore" : queryset_dong_20232[0]["개업_점포_수"],
            "20233openstore" : queryset_dong_20233[0]["개업_점포_수"],
            "csql2" : op_Compared_to_the_same_quarter_last_year,
            "cpq2" :   op_compared_to_the_previous_quarter,
            "sbd2" : op_status_of_business_districts,
            "bd2" : op_business_districts
                    
        }
        
        
        
        # 폐업 점포수 
        cl_Compared_to_the_same_quarter_last_year =  queryset_dong_20233[0]["폐업_점포_수"] -  queryset_dong_20223[0]["폐업_점포_수"]
        cl_compared_to_the_previous_quarter = queryset_dong_20233[0]["폐업_점포_수"] -  queryset_dong_20232[0]["폐업_점포_수"]
        if cl_Compared_to_the_same_quarter_last_year > 0:
            cl_status_of_business_districts = "증가"
            cl_business_districts = "활발하"
        else : 
            cl_status_of_business_districts = "감소"
            cl_business_districts = "침체되"
        
        closed_shop = {
            "20223closestore" : queryset_dong_20223[0]["폐업_점포_수"],
            "20224closestore" : queryset_dong_20224[0]["폐업_점포_수"],
            "20231closestore" : queryset_dong_20231[0]["폐업_점포_수"],
            "20232closestore" : queryset_dong_20232[0]["폐업_점포_수"],
            "20233closestore" : queryset_dong_20233[0]["폐업_점포_수"],
            "csql3" : cl_Compared_to_the_same_quarter_last_year,
            "cpq3" :   cl_compared_to_the_previous_quarter,
            "sbd3" : cl_status_of_business_districts,
            "bd3" : cl_business_districts
        }
        
        
        
        
        
        #매출
        
        
        #주거 인구

        residential_population = {
            "20223residential_population" : queryset_dong_20223[0]["총_상주인구_수"],
            "20224residential_population" : queryset_dong_20224[0]["총_상주인구_수"],
            "20231residential_population" : queryset_dong_20231[0]["총_상주인구_수"],
            "20232residential_population" : queryset_dong_20232[0]["총_상주인구_수"],
            "20233residential_population" : queryset_dong_20233[0]["총_상주인구_수"],
        }


        
        #배후지
        
        # 관공서
        government_office = queryset_dong_20233[0].get("관공서_수", 0)
        # 금융기관
        financial_institution = queryset_dong_20233[0].get("은행_수", 0)
        # 병원
        hospital = queryset_dong_20233[0].get("종합병원_수", 0) + queryset_dong_20233[0].get("일반_병원_수", 0)
        # 학교
        school = queryset_dong_20233[0].get("유치원_수", 0) + queryset_dong_20233[0].get("초등학교_수", 0)+ queryset_dong_20233[0].get("중학교_수", 0)+ queryset_dong_20233[0].get("고등학교_수", 0) +queryset_dong_20233[0].get("대학교_수", 0)
        # 유통점
        distribution_store = queryset_dong_20233[0].get("백화점_수", 0)+ queryset_dong_20233[0].get("슈퍼마켓_수", 0)
        # 극장
        theaters = queryset_dong_20233[0].get("극장_수", 0)
        # 숙박시설
        accommodation_facilities = queryset_dong_20233[0].get("숙박_시설_수", 0)
        # 교통시설
        Transportation_facilities = queryset_dong_20233[0].get("공항_수", 0) + queryset_dong_20233[0].get("철도_역_수", 0) + queryset_dong_20233[0].get("버스_터미널_수", 0) + queryset_dong_20233[0].get("지하철_역_수", 0) +queryset_dong_20233[0].get("버스_정거장_수", 0)
        
        
        
        background = {
            "go" : int(government_office),
            "fi" : int(financial_institution),
            "ho" : int(hospital),
            "sc" : int(school),
            "ds" : int(distribution_store) ,
            "th" : int(theaters),
            "ac" : int(accommodation_facilities),
            "tf" : int(Transportation_facilities)
        }
        
        sorted_background = sorted(background.items(), key=lambda x: x[1], reverse=True)

        # 상위 3개 항목을 추출
        top3 = sorted_background[:3]

        

        #소비트렌드

        #식료품    
        groceries_total_amount = int(queryset_dong_20233[0]["식료품_지출_총금액"] //10000)
        #의류
        Clothing_spending_total_amount = int(queryset_dong_20233[0]["의류_신발_지출_총금액"] //10000)

        #생활용품
        Household_goods_spending_total_amount = int(queryset_dong_20233[0]["생활용품_지출_총금액"] //10000)

        #의료비
        Medical_expenses_spending_total_amount = int(queryset_dong_20233[0]["의료비_지출_총금액"] //10000)

        #교통
        Transportation_spending_total_amount = int(queryset_dong_20233[0]["교통_지출_총금액"] //10000)

        # 교육
        Education_spending_total_amount = int(queryset_dong_20233[0]["교육_지출_총금액"] //10000)

        # 유흥
        entertainment_spending_total_amount = int(queryset_dong_20233[0]["유흥_지출_총금액"] //10000)

        #여가
        Leisure_culture_spending_total_amount = int(queryset_dong_20233[0]["여가_문화_지출_총금액"] //10000)

        #기타
        Other_spending_total_amount = int(queryset_dong_20233[0]["기타_지출_총금액"] //10000) 

        #음식
        Food_spending_total_amount = int(queryset_dong_20233[0]["음식_지출_총금액"] //10000) 

        # 총합
        total_amount = (groceries_total_amount + Clothing_spending_total_amount + Household_goods_spending_total_amount +
                           Medical_expenses_spending_total_amount +  Transportation_spending_total_amount +
                            Education_spending_total_amount + entertainment_spending_total_amount +
                                Leisure_culture_spending_total_amount + Other_spending_total_amount + Food_spending_total_amount)
        
        consumption_trend = {
            "food" :  round(((groceries_total_amount+Food_spending_total_amount) / total_amount *100),1) ,
            "Clothing" : round(( Clothing_spending_total_amount / total_amount *100),1),
            "Household" : round(( Household_goods_spending_total_amount / total_amount *100),1),
            "Medical" : round(( Medical_expenses_spending_total_amount / total_amount *100),1),
            "Transportation" : round(( Transportation_spending_total_amount / total_amount *100),1),
            "Education" : round(( Education_spending_total_amount / total_amount *100),1),
            "entertainment" : round(( entertainment_spending_total_amount / total_amount *100),1),
            "Leisure" : round(( Leisure_culture_spending_total_amount / total_amount *100),1),
            "Other" : round(( Other_spending_total_amount / total_amount *100),1),
        }

        max_value_key = max(consumption_trend, key=consumption_trend.get)
        
        if max_value_key == "food":
            most_trend ="음식"
        if max_value_key == "Clothing":
            most_trend ="의류"
        if max_value_key == "Household":
            most_trend ="생활용품"
        if max_value_key == "Medical":
            most_trend ="의료"
        if max_value_key == "Transportation":
            most_trend ="교통"
        if max_value_key == "Education":
            most_trend ="교육"
        if max_value_key == "entertainment":
            most_trend ="문화"
        if max_value_key == "Leisure":
            most_trend ="여가"
        if max_value_key == "Other":
            most_trend ="기타"
        
        response_data = {
            "자치구내 동 개수"  : dong_count,
            "점포순위" : dong_rank_data[0],
            "매출순위" : dong_rank_data[1],
            "유동인구순위" : dong_rank_data[2],
            "전분기대비매출액" : general_opinion[0],
            "전년도분기대비매출액" : general_opinion[1],

            "best 매출 성별 연령대" : sales_data[0],
            "best 매출 요일" : sales_data[1],
            "best 매출 시간대" : sales_data[2],
            "best 유동 성별 인구" : floating_population[0],
            "best 유동 연령대 인구" : floating_population[1],
            "best 유동 요일 인구" : floating_population[2],
            "best 유동 시간대 인구" : floating_population[3],

            "20223 점포수" : store_count["20223store_count"],
            "20224 점포수" : store_count["20224store_count"],
            "20231 점포수" : store_count["20231store_count"],
            "20232 점포수" : store_count["20232store_count"],
            "20233 점포수" : store_count["20233store_count"],
            "전년도 점포수 동분기 비교 수치 " : store_count["csql1"],
            "전분기 점포수 비교 수치 " : store_count["cpq1"],
            "점포수 증/감 텍스트" : store_count["sbd1"],
            "점포수 발/쇠 텍스트" : store_count["bd1"],

            "20223 개업점포수" : open_shop["20223openstore"],
            "20224 개업점포수" : open_shop["20224openstore"],
            "20231 개업점포수" : open_shop["20231openstore"],
            "20232 개업점포수" : open_shop["20232openstore"],
            "20233 개업점포수" : open_shop["20233openstore"],
            "전년도 개업점포수 동분기 비교 수치 " : open_shop["csql2"],
            "전분기 개업점포수 비교 수치 " : open_shop["cpq2"],
            "개업점포수 증/감 텍스트" : open_shop["sbd2"],
            "개업점포수 발/쇠 텍스트" : open_shop["bd2"],

            "20223 폐업점포수" : closed_shop["20223closestore"],
            "20224 폐업점포수" : closed_shop["20224closestore"],
            "20231 폐업점포수" : closed_shop["20231closestore"],
            "20232 폐업점포수" : closed_shop["20232closestore"],
            "20233 폐업점포수" : closed_shop["20233closestore"],
            "전년도 폐업점포수 동분기 비교 수치 " : closed_shop["csql3"],
            "전분기 폐업점포수 비교 수치 " : closed_shop["cpq3"],
            "폐업점포수 증/감 텍스트" : closed_shop["sbd3"],
            "폐업점포수 발/쇠 텍스트" : closed_shop["bd3"],

            "관공서" : background["go"],
            "금융기관" : background["fi"],
            "병원" : background["ho"],
            "학교" : background["sc"],
            "유통점" : background["ds"],
            "극장" : background["th"],
            "숙박시설" : background["ac"],
            "교통시설" : background["tf"],
            "배후지 1등 텍스트" : top3[0][0],
            "배후지 2등 텍스트" : top3[1][0],
            "배후지 3등 텍스트" : top3[2][0],

            
            "20223 주거인구" : residential_population["20223residential_population"],
            "20224 주거인구" : residential_population["20224residential_population"],
            "20231 주거인구" : residential_population["20231residential_population"],
            "20232 주거인구" : residential_population["20232residential_population"],
            "20233 주거인구" : residential_population["20233residential_population"],

            "소비트렌드 음식" : consumption_trend["food"],
            "소비트렌드 의류" : consumption_trend["Clothing"],
            "소비트렌드 생활용품" : consumption_trend["Household"],
            "소비트렌드 의료" : consumption_trend["Medical"],
            "소비트렌드 교통" : consumption_trend["Transportation"],
            "소비트렌드 교육" : consumption_trend["Education"],
            "소비트렌드 문화" : consumption_trend["entertainment"],
            "소비트렌드 여가" : consumption_trend["Leisure"],
            "소비트렌드 기타" : consumption_trend["Other"],
            "소비트렌드 텍스트 ": most_trend
        }
        #queryset_dong_20233
        return Response(response_data, status=status.HTTP_200_OK)
        
        #return Response(response_data, status=status.HTTP_200_OK)
        
        


class MarketReportView(APIView):
    def get(self, request):
        market_data = MarketSortedDbFin.objects.all()
        serializer = MarketReportDataSerializer(market_data, many=True)
        return Response(serializer.data)

class market_report(APIView):
    
    def get(self, request):
        
        market = "회현역"
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
                    "여가_지출_총금액","문화_지출_총금액"
                    
                    
                    ]
        
        
        queryset_market_20233 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*col_data)
        
        queryset_market_20232 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20231 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20224 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20223 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20223 ,서비스_업종_코드_명 = business).values(*col_data)
        
        #queryset_market_20233 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).all()
        
        #queryset_market_20233 = MarketSortedDbFin.objects.all()
        
        #1. 종합의견

        # 상권 순위 계산
        temp_result = []
        
        queryset_dong_goo = MarketSortedDbFin.objects.filter(상권_코드_명 = market).values("자치구_코드_명")
        queryset_dong_list = MarketSortedDbFin.objects.filter(자치구_코드_명 = queryset_dong_goo[0]["자치구_코드_명"]).values("상권_코드_명")
        #queryset_dong_list = MarketSortedDbFin.objects.filter(자치구_코드_명 = queryset_dong_goo[0]["자치구_코드_명"]).all()
        
        unique_data = list({item['상권_코드_명']: item for item in queryset_dong_list}.values())
        
        #return Response(unique_data, status=status.HTTP_200_OK)
        
        dong_count= len(unique_data)

        dong_names = [entry["상권_코드_명"] for entry in unique_data]


        
        # 점포 매출액 유동인구
        dong_col = ["상권_코드_명","점포_수","당월_매출_금액","총_유동인구_수"]
        dong_rank = []
        for i in dong_names :
            queryset_dong_data = MarketSortedDbFin.objects.filter(상권_코드_명 = i,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*dong_col)
            dong_rank.append(queryset_dong_data)

        # 빈리스트 제거
        dong_rank = [entry for entry in dong_rank if entry]
        
        
        
        
        #dong rank 데이터
        dong_rank_data = []

        sorted_data = sorted(dong_rank, key=lambda x: x[0]["점포_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        

        sorted_data = sorted(dong_rank, key=lambda x: x[0]["당월_매출_금액"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["총_유동인구_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        

        #전분기
        Quarterly_sales = int((queryset_market_20233[0]["당월_매출_금액"] - queryset_market_20232[0]["당월_매출_금액"])//10000)

        #전년도 분기 대비
        Sales_compared_to_the_same_quarter_last_year = int((queryset_market_20233[0]["당월_매출_금액"] - queryset_market_20223[0]["당월_매출_금액"])//10000)

        
        #종합 의견

        general_opinion = [Quarterly_sales,Sales_compared_to_the_same_quarter_last_year]
        
        
        #general_opinion = [data]


        #1-1 best 매출
        #성별
        gender_max = "남성" if queryset_market_20233[0]["남성_매출_금액"] > queryset_market_20233[0]["여성_매출_금액"] else "여성"

        # 연령대 중 가장 매출이 많은 것 찾기
        age_groups = ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"]
        age_max = max(age_groups, key=lambda x: queryset_market_20233[0][f"{x}_매출_금액"])

        # 요일 중 가장 매출이 많은 것 찾기
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        day_max = max(days, key=lambda x: queryset_market_20233[0][f"{x}_매출_금액"])
        total_sales = sum(queryset_market_20233[0][f"{day}_매출_금액"] for day in ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])
        
        dat_percentages = round((queryset_market_20233[0][f"{day_max}_매출_금액"] /total_sales *100),1)

        # 시간대 중 가장 매출이 많은 것 찾기
        time_ranges = ["시간대_00_06", "시간대_06_11", "시간대_11_14", "시간대_14_17", "시간대_17_21", "시간대_21_24"]
        time_max = max(time_ranges, key=lambda x: queryset_market_20233[0][f"{x}_매출_금액"])


        best_gender_age_group = gender_max +"/" + re.sub("[^0-9]", "", age_max) +"대"
        best_sales_day = day_max+f"({dat_percentages}%)"
        best_sales_time = re.sub("[^0-9]", "", time_max)
        best_sales_time = best_sales_time[:2] + "~" + best_sales_time[2:] + "시"

        sales_data = [best_gender_age_group , best_sales_day , best_sales_time  ]

        #유동인구
        
        gender_max = "남성" if queryset_market_20233[0]["남성_유동인구_수"] > queryset_market_20233[0]["여성_유동인구_수"] else "여성"

        # 연령대 중 가장 인구이 많은 것 찾기
        age_groups = ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"]
        age_max = max(age_groups, key=lambda x: queryset_market_20233[0][f"{x}_유동인구_수"])
        total_age_population = sum(queryset_market_20233[0][f"{age}_유동인구_수"] for age in ["연령대_10", "연령대_20", "연령대_30", "연령대_40", "연령대_50", "연령대_60_이상"])
        age_percentages = round((queryset_market_20233[0][f"{age_max}_유동인구_수"] /total_age_population *100),1)

        # 요일 중 가장 인구이 많은 것 찾기
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        day_max = max(days, key=lambda x: queryset_market_20233[0][f"{x}_유동인구_수"])
        total_population = sum(queryset_market_20233[0][f"{day}_유동인구_수"] for day in ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])
        
        dat_percentages = round((queryset_market_20233[0][f"{day_max}_유동인구_수"] /total_population *100),1)

        # 시간대 중 가장 매출이 많은 것 찾기
        time_ranges = ["시간대_00_06", "시간대_06_11", "시간대_11_14", "시간대_14_17", "시간대_17_21", "시간대_21_24"]
        time_max = max(time_ranges, key=lambda x: queryset_market_20233[0][f"{x}_유동인구_수"])

        best_population_age_group =  re.sub("[^0-9]", "", age_max) +"대"+f"({age_percentages}%)"
        best_population_day = day_max+f"({dat_percentages}%)"
        best_population_time = re.sub("[^0-9]", "", time_max)
        best_population_time = best_population_time[:2] + "~" + best_population_time[2:] + "시"


        #유동인구
        floating_population = [gender_max , best_population_age_group ,best_population_day , best_population_time  ]



        
        #2.점포
        
        # 전년 동분기 대비
        Compared_to_the_same_quarter_last_year = queryset_market_20233[0]["점포_수"] - queryset_market_20223[0]["점포_수"]
        # 전분기 대비
        compared_to_the_previous_quarter = queryset_market_20233[0]["점포_수"] - queryset_market_20232[0]["점포_수"]
        
        if Compared_to_the_same_quarter_last_year > 0:
            status_of_business_districts = "증가"
            business_districts = "발달"
        else : 
            status_of_business_districts = "감소"
            business_districts = "쇠퇴"
            
        
        store_count = {
            "20223store_count" : queryset_market_20223[0]["점포_수"],
            "20224store_count" : queryset_market_20224[0]["점포_수"],
            "20231store_count" : queryset_market_20231[0]["점포_수"],
            "20232store_count" : queryset_market_20232[0]["점포_수"],
            "20233store_count" : queryset_market_20233[0]["점포_수"],
            #전년 동분기 수치
            "csql1" : Compared_to_the_same_quarter_last_year,
            # 전 분기 수치
            "cpq1" :   compared_to_the_previous_quarter,
            # 안내 텍스트
            "sbd1" : status_of_business_districts,
            "bd1" : business_districts
        }
        
        # 개업 점포수 
        op_Compared_to_the_same_quarter_last_year =  queryset_market_20233[0]["개업_점포_수"] -  queryset_market_20223[0]["개업_점포_수"]
        op_compared_to_the_previous_quarter = queryset_market_20233[0]["개업_점포_수"] -  queryset_market_20232[0]["개업_점포_수"]
        if op_Compared_to_the_same_quarter_last_year > 0:
            op_status_of_business_districts = "증가"
            op_business_districts = "활발하"
        else : 
            op_status_of_business_districts = "감소"
            op_business_districts = "침체되"
            
        open_shop = {
            "20223openstore" : queryset_market_20223[0]["개업_점포_수"],
            "20224openstore" : queryset_market_20224[0]["개업_점포_수"],
            "20231openstore" : queryset_market_20231[0]["개업_점포_수"],
            "20232openstore" : queryset_market_20232[0]["개업_점포_수"],
            "20233openstore" : queryset_market_20233[0]["개업_점포_수"],
            "csql2" : op_Compared_to_the_same_quarter_last_year,
            "cpq2" :   op_compared_to_the_previous_quarter,
            "sbd2" : op_status_of_business_districts,
            "bd2" : op_business_districts
                    
        }
        
        
        
        # 폐업 점포수 
        cl_Compared_to_the_same_quarter_last_year =  queryset_market_20233[0]["폐업_점포_수"] -  queryset_market_20223[0]["폐업_점포_수"]
        cl_compared_to_the_previous_quarter = queryset_market_20233[0]["폐업_점포_수"] -  queryset_market_20232[0]["폐업_점포_수"]
        if cl_Compared_to_the_same_quarter_last_year > 0:
            cl_status_of_business_districts = "증가"
            cl_business_districts = "활발하"
        else : 
            cl_status_of_business_districts = "감소"
            cl_business_districts = "침체되"
        
        closed_shop = {
            "20223closestore" : queryset_market_20223[0]["폐업_점포_수"],
            "20224closestore" : queryset_market_20224[0]["폐업_점포_수"],
            "20231closestore" : queryset_market_20231[0]["폐업_점포_수"],
            "20232closestore" : queryset_market_20232[0]["폐업_점포_수"],
            "20233closestore" : queryset_market_20233[0]["폐업_점포_수"],
            "csql3" : cl_Compared_to_the_same_quarter_last_year,
            "cpq3" :   cl_compared_to_the_previous_quarter,
            "sbd3" : cl_status_of_business_districts,
            "bd3" : cl_business_districts
        }
        
        
        
        
        
        #매출
        
        
        #주거 인구

        residential_population = {
            "20223residential_population" : queryset_market_20223[0]["총_상주인구_수"],
            "20224residential_population" : queryset_market_20224[0]["총_상주인구_수"],
            "20231residential_population" : queryset_market_20231[0]["총_상주인구_수"],
            "20232residential_population" : queryset_market_20232[0]["총_상주인구_수"],
            "20233residential_population" : queryset_market_20233[0]["총_상주인구_수"],
        }


        
        #배후지
        
        # 관공서
        government_office = queryset_market_20233[0].get("관공서_수", 0)
        # 금융기관
        financial_institution = queryset_market_20233[0].get("은행_수", 0)
        # 병원
        hospital = queryset_market_20233[0].get("종합병원_수", 0) + queryset_market_20233[0].get("일반_병원_수", 0)
        # 학교
        school = queryset_market_20233[0].get("유치원_수", 0) + queryset_market_20233[0].get("초등학교_수", 0)+ queryset_market_20233[0].get("중학교_수", 0)+ queryset_market_20233[0].get("고등학교_수", 0) +queryset_market_20233[0].get("대학교_수", 0)
        # queryset_market_20233
        distribution_store = queryset_market_20233[0].get("백화점_수", 0)+ queryset_market_20233[0].get("슈퍼마켓_수", 0)
        # 극장
        theaters = queryset_market_20233[0].get("극장_수", 0)
        # 숙박시설
        accommodation_facilities = queryset_market_20233[0].get("숙박_시설_수", 0)
        # 교통시설
        Transportation_facilities = queryset_market_20233[0].get("공항_수", 0) + queryset_market_20233[0].get("철도_역_수", 0) + queryset_market_20233[0].get("버스_터미널_수", 0) + queryset_market_20233[0].get("지하철_역_수", 0) +queryset_market_20233[0].get("버스_정거장_수", 0)
        
        
        
        background = {
            "go" : int(government_office),
            "fi" : int(financial_institution),
            "ho" : int(hospital),
            "sc" : int(school),
            "ds" : int(distribution_store) ,
            "th" : int(theaters),
            "ac" : int(accommodation_facilities),
            "tf" : int(Transportation_facilities)
        }
        
        sorted_background = sorted(background.items(), key=lambda x: x[1], reverse=True)

        # 상위 3개 항목을 추출
        top3 = sorted_background[:3]

    

        #소비트렌드

        #식료품    
        groceries_total_amount = int(queryset_market_20233[0]["식료품_지출_총금액"] //10000)
        #의류
        Clothing_spending_total_amount = int(queryset_market_20233[0]["의류_신발_지출_총금액"] //10000)

        #생활용품
        Household_goods_spending_total_amount = int(queryset_market_20233[0]["생활용품_지출_총금액"] //10000)

        #의료비
        Medical_expenses_spending_total_amount = int(queryset_market_20233[0]["의료비_지출_총금액"] //10000)

        #교통
        Transportation_spending_total_amount = int(queryset_market_20233[0]["교통_지출_총금액"] //10000)

        # 교육
        Education_spending_total_amount = int(queryset_market_20233[0]["교육_지출_총금액"] //10000)

        # 유흥
        entertainment_spending_total_amount = int(queryset_market_20233[0]["유흥_지출_총금액"] //10000)

        #여가
        Leisure_culture_spending_total_amount = int(queryset_market_20233[0]["여가_지출_총금액"] //10000)

        #문화
        Culture_spending_total_amount = int(queryset_market_20233[0]["문화_지출_총금액"] //10000) 

        
        # 총합
        total_amount = (groceries_total_amount + Clothing_spending_total_amount + Household_goods_spending_total_amount +
                           Medical_expenses_spending_total_amount +  Transportation_spending_total_amount +
                            Education_spending_total_amount + entertainment_spending_total_amount +
                                Leisure_culture_spending_total_amount + Culture_spending_total_amount )
        
        consumption_trend = {
            "food" :  round(((groceries_total_amount) / total_amount *100),1) ,
            "Clothing" : round(( Clothing_spending_total_amount / total_amount *100),1),
            "Household" : round(( Household_goods_spending_total_amount / total_amount *100),1),
            "Medical" : round(( Medical_expenses_spending_total_amount / total_amount *100),1),
            "Transportation" : round(( Transportation_spending_total_amount / total_amount *100),1),
            "Education" : round(( Education_spending_total_amount / total_amount *100),1),
            "entertainment" : round(( entertainment_spending_total_amount / total_amount *100),1),
            "Leisure" : round(( Leisure_culture_spending_total_amount / total_amount *100),1),
            "Culture" : round(( Culture_spending_total_amount / total_amount *100),1),
        }

        max_value_key = max(consumption_trend, key=consumption_trend.get)
        
        if max_value_key == "food":
            most_trend ="음식"
        if max_value_key == "Clothing":
            most_trend ="의류"
        if max_value_key == "Household":
            most_trend ="생활용품"
        if max_value_key == "Medical":
            most_trend ="의료"
        if max_value_key == "Transportation":
            most_trend ="교통"
        if max_value_key == "Education":
            most_trend ="교육"
        if max_value_key == "entertainment":
            most_trend ="문화"
        if max_value_key == "Leisure":
            most_trend ="여가"
        if max_value_key == "Culture":
            most_trend ="문화"
        
        response_data = {
            "점포순위" : dong_rank_data[0],
            "매출순위" : dong_rank_data[1],
            "유동인구순위" : dong_rank_data[2],
            "전분기대비매출액" : general_opinion[0],
            "전년도분기대비매출액" : general_opinion[1],

            "best 매출 성별 연령대" : sales_data[0],
            "best 매출 요일" : sales_data[1],
            "best 매출 시간대" : sales_data[2],
            "best 유동 성별 인구" : floating_population[0],
            "best 유동 연령대 인구" : floating_population[1],
            "best 유동 요일 인구" : floating_population[2],
            "best 유동 시간대 인구" : floating_population[3],

            "20223 점포수" : store_count["20223store_count"],
            "20224 점포수" : store_count["20224store_count"],
            "20231 점포수" : store_count["20231store_count"],
            "20232 점포수" : store_count["20232store_count"],
            "20233 점포수" : store_count["20233store_count"],
            "전년도 점포수 동분기 비교 수치 " : store_count["csql1"],
            "전분기 점포수 비교 수치 " : store_count["cpq1"],
            "점포수 증/감 텍스트" : store_count["sbd1"],
            "점포수 발/쇠 텍스트" : store_count["bd1"],

            "20223 개업점포수" : open_shop["20223openstore"],
            "20224 개업점포수" : open_shop["20224openstore"],
            "20231 개업점포수" : open_shop["20231openstore"],
            "20232 개업점포수" : open_shop["20232openstore"],
            "20233 개업점포수" : open_shop["20233openstore"],
            "전년도 개업점포수 동분기 비교 수치 " : open_shop["csql2"],
            "전분기 개업점포수 비교 수치 " : open_shop["cpq2"],
            "개업점포수 증/감 텍스트" : open_shop["sbd2"],
            "개업점포수 발/쇠 텍스트" : open_shop["bd2"],

            "20223 폐업점포수" : closed_shop["20223closestore"],
            "20224 폐업점포수" : closed_shop["20224closestore"],
            "20231 폐업점포수" : closed_shop["20231closestore"],
            "20232 폐업점포수" : closed_shop["20232closestore"],
            "20233 폐업점포수" : closed_shop["20233closestore"],
            "전년도 폐업점포수 동분기 비교 수치 " : closed_shop["csql3"],
            "전분기 폐업점포수 비교 수치 " : closed_shop["cpq3"],
            "폐업점포수 증/감 텍스트" : closed_shop["sbd3"],
            "폐업점포수 발/쇠 텍스트" : closed_shop["bd3"],

            "관공서" : background["go"],
            "금융기관" : background["fi"],
            "병원" : background["ho"],
            "학교" : background["sc"],
            "유통점" : background["ds"],
            "극장" : background["th"],
            "숙박시설" : background["ac"],
            "교통시설" : background["tf"],
            "배후지 1등 텍스트" : top3[0][0],
            "배후지 2등 텍스트" : top3[1][0],
            "배후지 3등 텍스트" : top3[2][0],

            
            "20223 주거인구" : residential_population["20223residential_population"],
            "20224 주거인구" : residential_population["20224residential_population"],
            "20231 주거인구" : residential_population["20231residential_population"],
            "20232 주거인구" : residential_population["20232residential_population"],
            "20233 주거인구" : residential_population["20233residential_population"],

            "소비트렌드 음식" : consumption_trend["food"],
            "소비트렌드 의류" : consumption_trend["Clothing"],
            "소비트렌드 생활용품" : consumption_trend["Household"],
            "소비트렌드 의료" : consumption_trend["Medical"],
            "소비트렌드 교통" : consumption_trend["Transportation"],
            "소비트렌드 교육" : consumption_trend["Education"],
            "소비트렌드 문화" : consumption_trend["entertainment"],
            "소비트렌드 여가" : consumption_trend["Leisure"],
            "소비트렌드 문화" : consumption_trend["Culture"],
            "소비트렌드 텍스트 ": most_trend
        }

        return Response(response_data, status=status.HTTP_200_OK)
        



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
    
