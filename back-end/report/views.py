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
from analysis.models import DongServiceDataEstimateTestFullFin, MarketServiceDataEstimateTestFull
# Create your views here.


# 동 보고서 api 
class dong_report(APIView):
    
    
    # get 입력시
    def get(self, request, *args, **kwargs):
        
        #해당 인자로 동과 업종 입력
        dong = unquote(kwargs['dong'])
        business = unquote(kwargs['business'])
        
        # dong = DongServiceDataEstimateTestFullFin.objects.filter(행정동_코드=dong).first().행정동_코드_명
        
        # business = DongServiceDataEstimateTestFullFin.objects.filter(서비스_업종_코드 = business).first().서비스_업종_코드_명
        
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
        
        # 20223 ~ 20233년도 데이터 가져옴 
        queryset_dong_20233 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20232 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20231 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20224 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_dong_20223 = DongSortedDbFin.objects.filter(행정동_코드_명 = dong,기준_년분기_코드 = 20223 ,서비스_업종_코드_명 = business).values(*col_data)
        
        #1. 종합의견

        # 동 순위 계산
        queryset_dong_goo = SeoulRent.objects.filter(dong_name = dong).values("시군구명")
        queryset_dong_list = SeoulRent.objects.filter(시군구명 = queryset_dong_goo[0]["시군구명"]).values("dong_name")
        
        dong_count= len(queryset_dong_list)

        dong_names = [entry["dong_name"] for entry in queryset_dong_list]

        # 점포 매출액 유동인구
        dong_col = ["행정동_코드_명","점포_수","당월_매출_금액","총_유동인구_수"]
        dong_rank = []
        for i in dong_names :
            queryset_dong_data = DongSortedDbFin.objects.filter(행정동_코드_명 = i,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*dong_col)
            dong_rank.append(queryset_dong_data)

        # 빈리스트 제거
        dong_rank = [entry for entry in dong_rank if entry]
        
        #dong rank 데이터 넣기 위한 리스트
        dong_rank_data = []


        # 해당 구에서 해당 동의 점포수 순위
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["점포_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        
        # 해당 구에서 해당 동의 매출금액 순위
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["당월_매출_금액"], reverse=True)
        total_sales = sum(entry[0]["당월_매출_금액"] for entry in sorted_data)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        
        # 해당 구에서 해당 동의 유동인구 순위
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["총_유동인구_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["행정동_코드_명"] == dong), None)
        dong_rank_data.append(index_of_dong+1)
        

        #전분기
        Quarterly_sales = int((queryset_dong_20233[0]["당월_매출_금액"] - queryset_dong_20232[0]["당월_매출_금액"])//10000//dong_count)

        #전년도 분기 대비
        Sales_compared_to_the_same_quarter_last_year = int((queryset_dong_20233[0]["당월_매출_금액"] - queryset_dong_20223[0]["당월_매출_금액"])//10000//dong_count)

        #현재 평균 매출
        now_sales = int(queryset_dong_20233[0]["당월_매출_금액"] //10000//dong_count)
        
        #매출 증감 관련 텍스트
        if (total_sales / dong_count) > now_sales :
            sales_text = "감소"
        else :
            sales_text = "증가"


    

        #전분기 유동 인구 

        Quarterly_floating_population =  queryset_dong_20233[0]["총_유동인구_수"] -  queryset_dong_20232[0]["총_유동인구_수"]

        # 전년도 분기 대비 유동인구 
        floating_population_compared_to_the_same_quarter_last_year = queryset_dong_20233[0]["총_유동인구_수"] -  queryset_dong_20223[0]["총_유동인구_수"]

        #현재 유동 인구
        now_floating_population = queryset_dong_20233[0]["총_유동인구_수"]

        #종합 의견
        # 전분기,현재 ,전년도 분기 대비 (매출 금액 , 유동인구)
        general_opinion = [Quarterly_sales,Sales_compared_to_the_same_quarter_last_year,now_sales ,Quarterly_floating_population ,
                           floating_population_compared_to_the_same_quarter_last_year ,now_floating_population ]
        

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


        # best 매출 관련 텍스트 처리
        best_gender_age_group = gender_max +"/" + re.sub("[^0-9]", "", age_max) +"대"
        best_sales_day = day_max+f"({dat_percentages}%)"
        best_sales_time = re.sub("[^0-9]", "", time_max)
        best_sales_time = best_sales_time[:2] + "~" + best_sales_time[2:] + "시"
        
        # best 매출 그룹 =  성별+나이 , 요일 , 시간 
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

        
        # 유동인구 관련 텍스트 처리
        best_population_age_group =  re.sub("[^0-9]", "", age_max) +"대"+f"({age_percentages}%)"
        best_population_day = day_max+f"({dat_percentages}%)"
        best_population_time = re.sub("[^0-9]", "", time_max)
        best_population_time = best_population_time[:2] + "~" + best_population_time[2:] + "시"


        #유동인구
        #best 유동인구 관련 텍스트 , 성별, 나이,요일,시간
        best_floating_population = [gender_max , best_population_age_group ,best_population_day , best_population_time  ]



        
        #2.점포
        
        # 전년 동분기 대비
        Compared_to_the_same_quarter_last_year = queryset_dong_20233[0]["점포_수"] - queryset_dong_20223[0]["점포_수"]
        # 전분기 대비
        compared_to_the_previous_quarter = queryset_dong_20233[0]["점포_수"] - queryset_dong_20232[0]["점포_수"]
        
        
        # 점포 관련 텍스트 
        if Compared_to_the_same_quarter_last_year > 0:
            status_of_business_districts = "증가"
            business_districts = "발달"
        else : 
            status_of_business_districts = "감소"
            business_districts = "쇠퇴"
            
        # 점포 관련 데이터 모음
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
        
        # 개업 관련 텍스트 
        if op_Compared_to_the_same_quarter_last_year > 0:
            op_status_of_business_districts = "증가"
            op_business_districts = "활발하"
        else : 
            op_status_of_business_districts = "감소"
            op_business_districts = "침체되"
            
        # 개업 점포수 데이터 모음
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
        
        # 폐업 점포수 관련 증감 텍스트
        if cl_Compared_to_the_same_quarter_last_year > 0:
            cl_status_of_business_districts = "증가"
            cl_business_districts = "활발하"
        else : 
            cl_status_of_business_districts = "감소"
            cl_business_districts = "침체되"
        
        
        # 폐업 관련 데이터 정보 모음
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
        
        
        
        # 2022년 3분기~ 2023년 3분기 유동인구  데이터 모음
        floating_population = {
            "20223floating_population" : int(queryset_dong_20223[0]["총_유동인구_수"]),
            "20224floating_population" : int(queryset_dong_20224[0]["총_유동인구_수"]),
            "20231floating_population" : int(queryset_dong_20231[0]["총_유동인구_수"]),
            "20232floating_population" : int(queryset_dong_20232[0]["총_유동인구_수"]),
            "20233floating_population" : int(queryset_dong_20233[0]["총_유동인구_수"]),
            
        }

        # 유동인구 증감 텍스트
        if floating_population["20233floating_population"] - floating_population["20223floating_population"] > 0 :
            floating_population_text = "증가"
        else :
            floating_population_text = "감소"
        
        #주거 인구
        # 2022년 3분기~ 2023년 3분기 주거인구  데이터 모음
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
        
        
        # 배후지 인프라 갯수
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
        
        # 배후지 인프라 개수 순으로 정렬
        sorted_background = sorted(background.items(), key=lambda x: x[1], reverse=True)

        # 상위 3개 항목을 추출
        top3 = sorted_background[:3]

        # 상위 3개 항목을 관련 텍스트로 변환
        for i in range(len(top3)):
            if top3[i][0] == "go":
                top3[i] = ("관공서", top3[i][1])
            elif top3[i][0] == "fi":
                top3[i] = ("금융기관", top3[i][1])
            elif top3[i][0] == "ho":
                top3[i] = ("병원", top3[i][1])
            elif top3[i][0] == "sc":
                top3[i] = ("학교", top3[i][1])
            elif top3[i][0] == "ds":
                top3[i] = ("유통점", top3[i][1])
            elif top3[i][0] == "th":
                top3[i] = ("극장", top3[i][1])
            elif top3[i][0] == "ac":
                top3[i] = ("숙박시설", top3[i][1])
            elif top3[i][0] == "tf":
                top3[i] = ("교통시설", top3[i][1])        
    

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
        
        # 소비 트렌드 %로 변환후 저장
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

        # 가장 큰 항목 비율 찾기
        max_value_key = max(consumption_trend, key=consumption_trend.get)
        
        
        # 가장 큰 항목의 비율의 항목을 텍스트로 저장
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
            most_trend ="오락"
        if max_value_key == "Leisure":
            most_trend ="여가"
        if max_value_key == "Other":
            most_trend ="기타"
        
        
        # 반환 데이터 모음
        response_data = {
            # 동이름 , 해당 구의 동 개수
            "dongname" : dong,
            "dongcount" : dong_count,

            #매출, 유동인구 관련 텍스트
            "saletext" : sales_text,
            "floatingpopulationtext" : floating_population_text,

            #해당 동의 순위 데이터
            "storeranking" : dong_rank_data[0],
            "saleranking" : dong_rank_data[1],
            "Floating_population_ranking" : dong_rank_data[2],
            
            # 해당 동의 전분기,현재분기,전년도 대비 분기 매출데이터
            "Quarterlysales" : general_opinion[0],
            "nowsales" : general_opinion[2],
            "Salescomparedtothesamequarterlastyear" : general_opinion[1],

            # 해당 동의 전분기,현재분기,전년도 대비 분기 유동인구데이터
            "Quarterlyfloatingpopulation" : general_opinion[3],
            "nowfloatingpopulation" : general_opinion[5],
            "floatingpopulationcomparedtothesamequarterlastyear" : general_opinion[4],

            # best 매출 텍스트 데이터
            "best_gender_age_group" : sales_data[0],
            "best_sales_day" : sales_data[1],
            "best_sales_time" : sales_data[2],

            # best 유동인구 텍스트 데이터
            "bestgendermax" : best_floating_population[0],
            "bestpopulationagegroup" : best_floating_population[1],
            "bestpopulationday" : best_floating_population[2],
            "bestpopulationtime" : best_floating_population[3],

            # 점포수 관련 데이터 및 안내 텍스트
            "20223store_count" : store_count["20223store_count"],
            "20224store_count" : store_count["20224store_count"],
            "20231store_count" : store_count["20231store_count"],
            "20232store_count" : store_count["20232store_count"],
            "20233store_count" : store_count["20233store_count"],
            "csql1" : store_count["csql1"],
            "cpq1" : store_count["cpq1"],
            "sbd1text" : store_count["sbd1"],
            "bd1text" : store_count["bd1"],

            # 개업수 관련 데이터 및 안내 텍스트
            "20223openstore" : open_shop["20223openstore"],
            "20224openstore" : open_shop["20224openstore"],
            "20231openstore" : open_shop["20231openstore"],
            "20232openstore" : open_shop["20232openstore"],
            "20233openstore" : open_shop["20233openstore"],
            "csql2" : open_shop["csql2"],
            "cpq2" : open_shop["cpq2"],
            "sbd2text" : open_shop["sbd2"],
            "bd2text" : open_shop["bd2"],

            # 폐업수 관련 데이터 및 안내 텍스트
            "20223closestore" : closed_shop["20223closestore"],
            "20224closestore" : closed_shop["20224closestore"],
            "20231closestore" : closed_shop["20231closestore"],
            "20232closestore" : closed_shop["20232closestore"],
            "20233closestore" : closed_shop["20233closestore"],
            "csql3" : closed_shop["csql3"],
            "cpq3" : closed_shop["cpq3"],
            "sbd3text" : closed_shop["sbd3"],
            "bd3text" : closed_shop["bd3"],

            #배후지 관련 시설 개수
            "Governmentoffices" : background["go"],
            "Financialinstitutions" : background["fi"],
            "hospital" : background["ho"],
            "school" : background["sc"],
            "Distribution" : background["ds"],
            "Theater" : background["th"],
            "Accommodation" : background["ac"],
            "TransportationFacility" : background["tf"],
            "backgroundfirsttext" : top3[0][0],
            "backgroundsecondtext" : top3[1][0],
            "backgroundthirdtext" : top3[2][0],

            # 분기별 유동 인구 데이터
            "20223floating_population" : floating_population["20223floating_population"],
            "20224floating_population" : floating_population["20224floating_population"],
            "20231floating_population" : floating_population["20231floating_population"],
            "20232floating_population" : floating_population["20232floating_population"],
            "20233floating_population" : floating_population["20233floating_population"],

            # 분기별 주거 인구 데이터
            "20223residential_population" : residential_population["20223residential_population"],
            "20224residential_population" : residential_population["20224residential_population"],
            "20231residential_population" : residential_population["20231residential_population"],
            "20232residential_population" : residential_population["20232residential_population"],
            "20233residential_population" : residential_population["20233residential_population"],

            # 소비 트렌드 데이터
            "trendfood" : consumption_trend["food"],
            "trendClothing" : consumption_trend["Clothing"],
            "trendHousehold" : consumption_trend["Household"],
            "trendMedical" : consumption_trend["Medical"],
            "trendTransportation" : consumption_trend["Transportation"],
            "trendEducation" : consumption_trend["Education"],
            "trendentertainment" : consumption_trend["entertainment"],
            "trendLeisure" : consumption_trend["Leisure"],
            "trendOther" : consumption_trend["Other"],
            
            # 가장 많은 소비 텍스트
            "trendText": most_trend
        }
            # 데이터 반환
        return Response(response_data, status=status.HTTP_200_OK)
        
# 상권 보고서 API
class market_report(APIView):
    
    
    # get 요청시
    def get(self, request, *args, **kwargs):
        
        # 받은 인자로 상권및 업종 구분
        market = unquote(kwargs["market"])
        business = unquote(kwargs["business"])
        
        # market = MarketServiceDataEstimateTestFull.objects.filter(상권_코드=market).first().상권_코드_명
        # business = MarketServiceDataEstimateTestFull.objects.filter(서비스_업종_코드=business).first().서비스_업종_코드_명
        
        # db에서 꺼내올 데이터
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
        
        # 분기별 해당 상권의 데이터를 가져옴
        queryset_market_20233 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20233 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20232 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20231 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20231 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20224 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20224 ,서비스_업종_코드_명 = business).values(*col_data)
        queryset_market_20223 = MarketSortedDbFin.objects.filter(상권_코드_명 = market,기준_년분기_코드 = 20223 ,서비스_업종_코드_명 = business).values(*col_data)
        
        
        #1. 종합의견

        # 구에서 상권 순위 계산
        
        queryset_dong_goo = MarketSortedDbFin.objects.filter(상권_코드_명 = market).values("자치구_코드_명")
        queryset_dong_list = MarketSortedDbFin.objects.filter(자치구_코드_명 = queryset_dong_goo[0]["자치구_코드_명"]).values("상권_코드_명")
        unique_data = list({item['상권_코드_명']: item for item in queryset_dong_list}.values())
        
        # 해당 상권 이름 모음
        dong_names = [entry["상권_코드_명"] for entry in unique_data]

        market_count= len(dong_names)

        # 점포 매출액 유동인구
        dong_col = ["상권_코드_명","점포_수","당월_매출_금액","총_유동인구_수"]
        dong_rank = []
        for i in dong_names :
            queryset_dong_data = MarketSortedDbFin.objects.filter(상권_코드_명 = i,기준_년분기_코드 = 20232 ,서비스_업종_코드_명 = business).values(*dong_col)
            dong_rank.append(queryset_dong_data)

        # 빈리스트 제거
        dong_rank = [entry for entry in dong_rank if entry]
                
        
        #상권 rank 데이터 , 해당 상권의 점포수,매출,유동인구 계산
        dong_rank_data = []

        sorted_data = sorted(dong_rank, key=lambda x: x[0]["점포_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["당월_매출_금액"], reverse=True)
        total_sales = sum(entry[0]["당월_매출_금액"] for entry in sorted_data)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        sorted_data = sorted(dong_rank, key=lambda x: x[0]["총_유동인구_수"], reverse=True)
        index_of_dong = next((index for index, entry in enumerate(sorted_data) if entry[0]["상권_코드_명"] == market), None)
        dong_rank_data.append(index_of_dong+1)
        
        
        #전분기 평균 매출
        Quarterly_sales = int((queryset_market_20233[0]["당월_매출_금액"] - queryset_market_20232[0]["당월_매출_금액"])//10000//market_count)

        #전년도 분기 대비 평균 매출
        Sales_compared_to_the_same_quarter_last_year = int((queryset_market_20233[0]["당월_매출_금액"] - queryset_market_20223[0]["당월_매출_금액"])//10000//market_count)

        #현재 평균 매출
        now_sales = int(queryset_market_20233[0]["당월_매출_금액"] //10000//market_count)
        
        # 매출 관련 텍스트
        if (total_sales / market_count) > now_sales :
            sales_text = "감소"
        else :
            sales_text = "증가"


        #전분기 유동 인구 
        Quarterly_floating_population =  queryset_market_20233[0]["총_유동인구_수"] -  queryset_market_20232[0]["총_유동인구_수"]

        # 전년도 분기 대비 유동인구 
        floating_population_compared_to_the_same_quarter_last_year = queryset_market_20233[0]["총_유동인구_수"] -  queryset_market_20223[0]["총_유동인구_수"]

        #현재 유동 인구
        now_floating_population = queryset_market_20233[0]["총_유동인구_수"]

        #종합 의견 데이터 모음 
        # 전분기 ,전년도대비 , 현재 순으로 매출,유동 인구  
        general_opinion = [Quarterly_sales,Sales_compared_to_the_same_quarter_last_year,now_sales ,Quarterly_floating_population ,
                           floating_population_compared_to_the_same_quarter_last_year ,now_floating_population ]
        

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

        # 매출 관련 텍스트 처리
        best_gender_age_group = gender_max +"/" + re.sub("[^0-9]", "", age_max) +"대"
        best_sales_day = day_max+f"({dat_percentages}%)"
        best_sales_time = re.sub("[^0-9]", "", time_max)
        best_sales_time = best_sales_time[:2] + "~" + best_sales_time[2:] + "시"

        # 매출 관련 텍스트 데이터 
        # 성별나이 , 요일 , 시간
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

        #유동인구 관련 텍스트 처리
        best_population_age_group =  re.sub("[^0-9]", "", age_max) +"대"+f"({age_percentages}%)"
        best_population_day = day_max+f"({dat_percentages}%)"
        best_population_time = re.sub("[^0-9]", "", time_max)
        best_population_time = best_population_time[:2] + "~" + best_population_time[2:] + "시"


        #유동인구 
        # 성별,나이,요일,시간
        best_floating_population = [gender_max , best_population_age_group ,best_population_day , best_population_time  ]

        #2.점포
        
        # 전년 동분기 대비
        Compared_to_the_same_quarter_last_year = queryset_market_20233[0]["점포_수"] - queryset_market_20223[0]["점포_수"]
        # 전분기 대비
        compared_to_the_previous_quarter = queryset_market_20233[0]["점포_수"] - queryset_market_20232[0]["점포_수"]
        
        #점포 관련 텍스트 처리
        if Compared_to_the_same_quarter_last_year > 0:
            status_of_business_districts = "증가"
            business_districts = "발달"
        else : 
            status_of_business_districts = "감소"
            business_districts = "쇠퇴"
            
        # 점포관련 텍스트 모음
        
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
        
        # 개업 점포 관련 텍스트 처리
        if op_Compared_to_the_same_quarter_last_year > 0:
            op_status_of_business_districts = "증가"
            op_business_districts = "활발하"
        else : 
            op_status_of_business_districts = "감소"
            op_business_districts = "침체되"
            
        # 개업 관련 텍스트 모음
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
        
        # 폐업 관련 텍스트 처리
        if cl_Compared_to_the_same_quarter_last_year > 0:
            cl_status_of_business_districts = "증가"
            cl_business_districts = "활발하"
        else : 
            cl_status_of_business_districts = "감소"
            cl_business_districts = "침체되"
        
        
        # 폐업 관련 데이터 모음
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
        
        
        
        
        # 분기별 유동인구 데이터 모음 
        floating_population = {
            "20223floating_population" : int(queryset_market_20223[0]["총_유동인구_수"]),
            "20224floating_population" : int(queryset_market_20224[0]["총_유동인구_수"]),
            "20231floating_population" : int(queryset_market_20231[0]["총_유동인구_수"]),
            "20232floating_population" : int(queryset_market_20232[0]["총_유동인구_수"]),
            "20233floating_population" : int(queryset_market_20233[0]["총_유동인구_수"]),
        }
        
        
        # 유동인구 증감 텍스트
        if floating_population["20233floating_population"] - floating_population["20223floating_population"] > 0 :
            floating_population_text = "증가"
        else :
            floating_population_text = "감소"

        
        #분기별 주거 인구 데이터 모음
        residential_population = {
            "20223residential_population" : int(queryset_market_20223[0]["총_상주인구_수"]),
            "20224residential_population" : int(queryset_market_20224[0]["총_상주인구_수"]),
            "20231residential_population" : int(queryset_market_20231[0]["총_상주인구_수"]),
            "20232residential_population" : int(queryset_market_20232[0]["총_상주인구_수"]),
            "20233residential_population" : int(queryset_market_20233[0]["총_상주인구_수"]),
        }


        
        #상권 배후지 관련 인프라 개수 가져오기
        
        # 관공서
        government_office = queryset_market_20233[0].get("관공서_수", 0)
        # 금융기관
        financial_institution = queryset_market_20233[0].get("은행_수", 0)
        # 병원
        hospital = queryset_market_20233[0].get("종합병원_수", 0) + queryset_market_20233[0].get("일반_병원_수", 0)
        # 학교
        school = queryset_market_20233[0].get("유치원_수", 0) + queryset_market_20233[0].get("초등학교_수", 0)+ queryset_market_20233[0].get("중학교_수", 0)+ queryset_market_20233[0].get("고등학교_수", 0) +queryset_market_20233[0].get("대학교_수", 0)
        # 유통점
        distribution_store = queryset_market_20233[0].get("백화점_수", 0)+ queryset_market_20233[0].get("슈퍼마켓_수", 0)
        # 극장
        theaters = queryset_market_20233[0].get("극장_수", 0)
        # 숙박시설
        accommodation_facilities = queryset_market_20233[0].get("숙박_시설_수", 0)
        # 교통시설
        Transportation_facilities = queryset_market_20233[0].get("공항_수", 0) + queryset_market_20233[0].get("철도_역_수", 0) + queryset_market_20233[0].get("버스_터미널_수", 0) + queryset_market_20233[0].get("지하철_역_수", 0) +queryset_market_20233[0].get("버스_정거장_수", 0)
        
        # 배후지 인프라 개수 모음
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
        
        # 개수순의로 정렬
        sorted_background = sorted(background.items(), key=lambda x: x[1], reverse=True)

        # 상위 3개 항목을 추출
        top3 = sorted_background[:3]

        # 상위 3개 항목 텍스트로 변환
        for i in range(len(top3)):
            if top3[i][0] == "go":
                top3[i] = ("관공서", top3[i][1])
            elif top3[i][0] == "fi":
                top3[i] = ("금융기관", top3[i][1])
            elif top3[i][0] == "ho":
                top3[i] = ("병원", top3[i][1])
            elif top3[i][0] == "sc":
                top3[i] = ("학교", top3[i][1])
            elif top3[i][0] == "ds":
                top3[i] = ("유통점", top3[i][1])
            elif top3[i][0] == "th":
                top3[i] = ("극장", top3[i][1])
            elif top3[i][0] == "ac":
                top3[i] = ("숙박시설", top3[i][1])
            elif top3[i][0] == "tf":
                top3[i] = ("교통시설", top3[i][1])        
    

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
        
        #소비 트렌드 모음
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

        # 가장 많은 비율을 가진 소비액 항목 찾기
        max_value_key = max(consumption_trend, key=consumption_trend.get)
        
        # 가장 많은 소비액을 가진 항목 텍스트를 저장
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
            most_trend ="오락"
        if max_value_key == "Leisure":
            most_trend ="여가"
        if max_value_key == "Culture":
            most_trend ="문화"
        
        # 반환 목록
        response_data = {
            # 상권이름 , 해당 구의 상권 개수
            "marketname" : market,
            "marketcount" : market_count,

            # 매출,유동인구 관련 텍스트
            "saletext" : sales_text,
            "floatingpopulationtext" : floating_population_text,

            # 해당 상권의 해당 구에서의 순위
            "storeranking" : dong_rank_data[0],
            "saleranking" : dong_rank_data[1],
            "Floating_population_ranking" : dong_rank_data[2],
            
            # 전분기,현재,전년도 대비 에 대한 매출 
            "Quarterlysales" : general_opinion[0],
            "nowsales" : general_opinion[2],
            "Salescomparedtothesamequarterlastyear" : general_opinion[1],

            # 전분기 , 현재 , 전년도 대비에 대한 유동인구
            "Quarterlyfloatingpopulation" : general_opinion[3],
            "nowfloatingpopulation" : general_opinion[5],
            "floatingpopulationcomparedtothesamequarterlastyear" : general_opinion[4],

            # best 매출 데이터 성별 요일 시간
            "best_gender_age_group" : sales_data[0],
            "best_sales_day" : sales_data[1],
            "best_sales_time" : sales_data[2],

            # best 유동인구 순위 성별 , 나이,요일, 시간대
            "bestgendermax" : best_floating_population[0],
            "bestpopulationagegroup" : best_floating_population[1],
            "bestpopulationday" : best_floating_population[2],
            "bestpopulationtime" : best_floating_population[3],

            # 해당 상권 점포수 관련 데이터
            "20223store_count" : store_count["20223store_count"],
            "20224store_count" : store_count["20224store_count"],
            "20231store_count" : store_count["20231store_count"],
            "20232store_count" : store_count["20232store_count"],
            "20233store_count" : store_count["20233store_count"],
            "csql1" : store_count["csql1"],
            "cpq1" : store_count["cpq1"],
            "sbd1text" : store_count["sbd1"],
            "bd1text" : store_count["bd1"],

            # 해당 개업 점포 관련 데이터 
            "20223openstore" : open_shop["20223openstore"],
            "20224openstore" : open_shop["20224openstore"],
            "20231openstore" : open_shop["20231openstore"],
            "20232openstore" : open_shop["20232openstore"],
            "20233openstore" : open_shop["20233openstore"],
            "csql2" : open_shop["csql2"],
            "cpq2" : open_shop["cpq2"],
            "sbd2text" : open_shop["sbd2"],
            "bd2text" : open_shop["bd2"],

            # 해당 폐업 점포관련 데이터
            "20223closestore" : closed_shop["20223closestore"],
            "20224closestore" : closed_shop["20224closestore"],
            "20231closestore" : closed_shop["20231closestore"],
            "20232closestore" : closed_shop["20232closestore"],
            "20233closestore" : closed_shop["20233closestore"],
            "csql3" : closed_shop["csql3"],
            "cpq3" : closed_shop["cpq3"],
            "sbd3text" : closed_shop["sbd3"],
            "bd3text" : closed_shop["bd3"],

            # 배후지 인프라 개수 데이터
            "Governmentoffices" : background["go"],
            "Financialinstitutions" : background["fi"],
            "hospital" : background["ho"],
            "school" : background["sc"],
            "Distribution" : background["ds"],
            "Theater" : background["th"],
            "Accommodation" : background["ac"],
            "TransportationFacility" : background["tf"],
            "backgroundfirsttext" : top3[0][0],
            "backgroundsecondtext" : top3[1][0],
            "backgroundthirdtext" : top3[2][0],

            # 분기별 유동인구
            "20223floating_population" : floating_population["20223floating_population"],
            "20224floating_population" : floating_population["20224floating_population"],
            "20231floating_population" : floating_population["20231floating_population"],
            "20232floating_population" : floating_population["20232floating_population"],
            "20233floating_population" : floating_population["20233floating_population"],

            # 분기별 주거인구
            "20223residential_population" : residential_population["20223residential_population"],
            "20224residential_population" : residential_population["20224residential_population"],
            "20231residential_population" : residential_population["20231residential_population"],
            "20232residential_population" : residential_population["20232residential_population"],
            "20233residential_population" : residential_population["20233residential_population"],

            #소비 트렌드 관련 데이터
            "trendfood" : consumption_trend["food"],
            "trendClothing" : consumption_trend["Clothing"],
            "trendHousehold" : consumption_trend["Household"],
            "trendMedical" : consumption_trend["Medical"],
            "trendTransportation" : consumption_trend["Transportation"],
            "trendEducation" : consumption_trend["Education"],
            "trendentertainment" : consumption_trend["entertainment"],
            "trendLeisure" : consumption_trend["Leisure"],
            "trendCulture" : consumption_trend["Culture"],
            "trendText": most_trend
        }
            # 데이터 반환
        return Response(response_data, status=status.HTTP_200_OK)
        
