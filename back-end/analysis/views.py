
from django.shortcuts import render
from urllib.parse import unquote
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
import pandas as pd
from .models import *
from .serializers import *

from pycaret.regression import *

# 추정 : 23년 3분기의 매출을 출력
# 예측 : 23년 4분기의 매출을 출력


#프랜차이즈 함수


# 유저가 입력한 자본금 내에서 창업가능한 가장 매출이 높은 프랜차이즈 브랜드 제공

def get_franchise_data_dong(dongname, sectors, seedmoney):
    
    # 각 행정동 별 상권들의 평균 임대료 
    rentcost = rent_cost_data(dongname)
    
    # if rentcost == -1: return None
    seedmoney = seedmoney*10
    
    franchise_col = ["브랜드명","평균매출금액","가맹금액","교육금액","보증금액","기타금액","합계금액"]
    
    seedmoney = seedmoney - (rentcost*11)
    
    original_dict = {
    '한식음식점': '한식',
    '커피-음료': '커피',
    '분식전문점': '분식',
    '호프-간이주점': '주점',
    '치킨전문점': '치킨',
    '중식음식점': '중식',
    '패스트푸드점': '패스트푸드',
    '제과점': '제과제빵',
    '일식음식점': '일식',
    '양식음식점': '서양식',
    '편의점': '편의점',
    '일반의류': None,
    '화장품': '화장품',
    '의약품': None,
    '일반교습학원': ['교육 (교과)', '교육 (외국어)'],
    '미용실': '미용'
    }
    
    
    queryset_franch1 = FranchiseData.objects.filter(중분류서비스 = original_dict[sectors], 합계금액__lte = seedmoney).order_by('평균매출금액').values(*franchise_col)
    
    franchise_sort_data = queryset_franch1[::-1]
    
    if rentcost == -1 or len(franchise_sort_data) < 1:
        fran_response_last = [None, None, None, None]
    elif len(franchise_sort_data) == 1:
        fran_response_last =   [rentcost, len(franchise_sort_data), franchise_sort_data[0], None]
    else:
        fran_response_last =   [rentcost, len(franchise_sort_data), franchise_sort_data[0], franchise_sort_data[1]]
    
    
    # 같은 브랜드가 중복되어 출력되는 것을 방지
    i=1
    if fran_response_last[2]['브랜드명'] == fran_response_last[3]['브랜드명']:
        for i in range(len(franchise_sort_data)):
            fran_response_last[2] = franchise_sort_data[1+i]
            fran_response_last[3] = franchise_sort_data[2+i]
            if fran_response_last[2]['브랜드명'] != fran_response_last[3]['브랜드명']:break
            
        
    
    
    return fran_response_last
    
    
    

# 입력을 행정동이 아닌 상권으로 할 경우 행정동으로 바꾸는 작업
def get_franchise_data_market(marketname, sectors, seedmoney):
    
    dongname = MarketSortedDbFin.objects.filter(상권_구분_코드_명 = marketname).first().행정동_코드_명
    
    result = get_franchise_data_dong(dongname, sectors, seedmoney)
    
    return result







# 행정동 단위 AI

class dong_ai(generics.GenericAPIView):
    serializer_class = AIReportSerializer
    
    # 자치구, 행정동, 업종, 자본금을 입력받아 AI 리포트의 데이터를 작성
    
    def get(self, request, *args, **kargs):
        
        # 입력받은 한글 데이터를 디코딩
        goo_name = unquote(self.kwargs['goo'])
        dong_name = unquote(self.kwargs['dong'])
        business_name = unquote(self.kwargs['business'])
        funds = self.kwargs['funds']
        

        # 코드 명을 코드로 변경
        goo= MarketSortedDbFin.objects.filter(자치구_코드_명=goo_name).first().자치구_코드
        dong = MarketSortedDbFin.objects.filter(행정동_코드_명=dong_name).first().행정동_코드
        business = MarketSortedDbFin.objects.filter(서비스_업종_코드_명 = business_name).first().서비스_업종_코드
        
        
        # 예측에 쓰이는 Feature 목록
        
        x_cols = ['행정동_코드', '서비스_업종_코드', '관공서_수', '은행_수', '종합병원_수', '일반_병원_수', '약국_수',
       '유치원_수', '초등학교_수', '중학교_수', '고등학교_수', '대학교_수', '백화점_수', '슈퍼마켓_수',
       '극장_수', '숙박_시설_수', '공항_수', '철도_역_수', '버스_터미널_수', '지하철_역_수', '버스_정거장_수',
       '연령대_10_직장_인구_수', '연령대_20_직장_인구_수', '연령대_30_직장_인구_수', '연령대_40_직장_인구_수',
       '연령대_50_직장_인구_수', '연령대_60_이상_직장_인구_수', '점포_수', '개업_율', '개업_점포_수',
       '폐업_률', '폐업_점포_수', '프랜차이즈_점포_수', '아파트_단지_수', '아파트_면적_66_제곱미터_미만_세대_수',
       '아파트_면적_66_제곱미터_세대_수', '아파트_면적_99_제곱미터_세대_수', '아파트_면적_132_제곱미터_세대_수',
       '아파트_면적_165_제곱미터_세대_수', '아파트_가격_1_억_미만_세대_수', '아파트_가격_1_억_세대_수',
       '아파트_가격_2_억_세대_수', '아파트_가격_3_억_세대_수', '아파트_가격_4_억_세대_수',
       '아파트_가격_5_억_세대_수', '아파트_가격_6_억_이상_세대_수', '아파트_평균_면적', '아파트_평균_시가',
       '월_평균_소득_금액', '식료품_지출_총금액', '의류_신발_지출_총금액', '생활용품_지출_총금액', '의료비_지출_총금액',
       '교통_지출_총금액', '교육_지출_총금액', '유흥_지출_총금액', '여가_문화_지출_총금액', '기타_지출_총금액',
       '음식_지출_총금액', '연령대_10_상주인구_수', '연령대_20_상주인구_수', '연령대_30_상주인구_수',
       '연령대_40_상주인구_수', '연령대_50_상주인구_수', '연령대_60_이상_상주인구_수', '아파트_가구_수',
       '비_아파트_가구_수', '연령대_10_유동인구_수', '연령대_20_유동인구_수', '연령대_30_유동인구_수',
       '연령대_40_유동인구_수', '연령대_50_유동인구_수', '연령대_60_이상_유동인구_수',
       '시간대_00_06_유동인구_수', '시간대_06_11_유동인구_수', '시간대_11_14_유동인구_수',
       '시간대_14_17_유동인구_수', '시간대_17_21_유동인구_수', '시간대_21_24_유동인구_수','분기', '코로나_여부', '전년도_점포별_평균_매출_금액']
        
        # estimate 23년 3분기 예측
        queryset_estimate = DongServiceDataEstimateTestFullFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values(*x_cols)
        queryset_estimate = queryset_estimate[0]
     
        data_pd = pd.DataFrame(queryset_estimate, index=[0])
        
        final_model = load_model("analysis/aimodel/dong_service_estimate_model1")
        prediction = predict_model(final_model, data = data_pd)
        estimate_result = prediction['prediction_label']
       
        # predict 23년 4분기 예측
           
        queryset_predict = DongServiceDataPredictTestFullFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values(*x_cols)
        queryset_predict = queryset_predict[0]
        
        data_pd = pd.DataFrame(queryset_predict, index=[0])
        
        final_model = load_model("analysis/aimodel/dong_service_pred_model1")
        prediction = predict_model(final_model, data = data_pd)
        predict_result = prediction['prediction_label']
        
        
        # 미리 계산해둔 shap 값 존재 여부 확인
        
        try:
            shapValue = DongServiceEstimateShapValues.objects.filter(행정동_코드 = dong, 서비스_업종_코드 = business).first()
            shapValue = DongServiceEstimateShapValuesSerializer(shapValue).data
            del shapValue['행정동_코드']
            del shapValue['서비스_업종_코드']
            
            shapValue = dict(sorted(shapValue.items(), key=lambda item: item[1], reverse=True))

            shapValueOutputTop5 = {}
            count = 0
            for key, item in shapValue.items():
                if item == 0:
                    continue
                shapValueOutputTop5[key] = item
                count += 1
                if count == 5:
                    break

            shapValueOutputBottom5 = {}
            count = 0
            for key, item in reversed(shapValue.items()):
                if item == 0:
                    continue
                shapValueOutputBottom5[key] = item
                count += 1
                if count == 5:
                    break
        except:
            
            # shap 값이 없을 시 None처리
            shapValueOutputTop5 = None
            shapValueOutputBottom5 = None    
            
            
        # 기준 년분기의 서울시 내 동일 업종의 점포별 평균 매출 금액을 계산
        goo = goo_name
        queryset_avg_seoul = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business).values("점포별_평균_매출_금액")
        avg_zero = 0
        count = 0
        
        
        
        for i in queryset_avg_seoul:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        seoul_avg = avg_zero/count
        
        seoul_diff = (estimate_result.values/seoul_avg)*100
        
        # 서울 전체 평균 매출을 기준으로 창업 지수 결정
        
        if seoul_diff >= 150:
            analysis = "양호"
        
        elif seoul_diff <= 50:
            analysis = "위험"
        else:
            analysis = "보통"
            
        if seoul_diff > 200:
            seoul_diff = 200
        
        jachigu = MarketSortedDbFin.objects.filter(행정동_코드 = dong).values('자치구_코드', '자치구_코드_명').first()
        
        
        # 해당 자치구 1, 2분기 점포별 평균 매출 금액 계산
        queryset_avg_1qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business, 자치구_코드 = jachigu['자치구_코드']).values("점포별_평균_매출_금액")
        queryset_avg_2qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20231, 서비스_업종_코드 = business, 자치구_코드 = jachigu['자치구_코드']).values("점포별_평균_매출_금액")
        
        avg_zero = 0
        count = 0
        for i in queryset_avg_1qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_1qb = avg_zero/count    
        
        avg_zero = 0
        count = 0
        for i in queryset_avg_2qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_2qb = avg_zero/count   
        
        # 해당 자치구 1, 2 분기 점포별 평균 매출 금액을 활용 AI리포트 내용 생성
        # 지역별 활성화 여부
        
        analysis_avg_diff = "증가" if (avg_2qb - avg_1qb) > 0 else "감소"
        analysis_active = "활성화" if (avg_2qb - avg_1qb) > 0 else "비활성화"
        
        
        
        # 작년 동분기와 현재의 창업 수 비교 발달 쇠퇴 여부
        queryset_opening = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values('점포_수')
        opening = queryset_opening[0]['점포_수']
        
        queryset_opening_lyb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 행정동_코드 = dong, 서비스_업종_코드 = business).values('점포_수')
        opening_lyb = queryset_opening_lyb[0]['점포_수']
        
        
        analysis_opening = "증가" if (opening - opening_lyb) > 0 else "감소"
        analysis_growth = "발달" if (opening - opening_lyb) > 0 else "쇠퇴"
        
        
        # 작년 동분기와 현재의 유동인구 수 비교
        queryset_mp_1yb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 행정동_코드 = dong, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp_1yb = queryset_mp_1yb[0]['총_유동인구_수']
        
        queryset_mp = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp = queryset_mp[0]['총_유동인구_수']
        
        
        analysis_mp = "증가" if (mp - mp_1yb) > 0 else "감소"
        
        
        
        # 매출이 비슷한 주변 지역 두 곳 선정
        queryset_similar = DongServiceEstimateY.objects.filter(서비스_업종_코드 = business).values('행정동_코드', 'prediction_label') 
        
        for i in queryset_similar:
            num = i['prediction_label']
            diff = abs(num - estimate_result.values)
            i['diff'] = diff
            
        sortedList = sorted(queryset_similar, key=lambda x: x['diff'], reverse=True)
        num1 = sortedList[0]
        num2 = sortedList[1]
        
        
        similar_dongs1 = DongSortedDbFin.objects.filter(행정동_코드 = num1['행정동_코드']).values('행정동_코드_명').first()
        similar_dongs2 = DongSortedDbFin.objects.filter(행정동_코드 = num2['행정동_코드']).values('행정동_코드_명').first()
        
        similar_dongs1_name = similar_dongs1['행정동_코드_명']
        similar_dongs1_pred = num1['prediction_label']
        similar_dongs1_diff = estimate_result.values - similar_dongs1_pred
        
        similar_dongs2_name = similar_dongs2['행정동_코드_명']
        similar_dongs2_pred = num2['prediction_label']
        similar_dongs2_diff = estimate_result.values - similar_dongs2_pred
        
        
        queryset_target_avg_1qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business, 행정동_코드 = dong).values("점포별_평균_매출_금액")
        
        avg_zero = 0
        count = 0
        for i in queryset_target_avg_1qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_target_1qb = avg_zero/count  
        
        
        # 자본금 내 가능한 매출이 가장 높은 프랜차이즈 두 곳 검색
        franchise = get_franchise_data_dong(dong_name, business_name, funds)
        
        # 매출에 긍정적 영향 최고 5개 와 부정적 영향 최고 5개를 선정
        
        shapValueOutputTop5 = {key: int(value) for key, value in shapValueOutputTop5.items()}
        shapValueOutputBottom5 = {key: int(value) for key, value in shapValueOutputBottom5.items()}
        
        # 프랜차이즈 창업 비용 항목들을 10000원 단위로 맞춤
        
        if franchise[2] != None:
            franchise[2] = {key: int(int(value) / 10) if key != '브랜드명' else value for key, value in franchise[2].items()}
        if franchise[3] != None:
            franchise[3] = {key: int(int(value) / 10) if key != '브랜드명' else value for key, value in franchise[3].items()}
        
        # print(franchise)
        
        # 리포트 내용 전송
        
        output_data = {"AI":"행정동",
                       "region":goo, 
                       "area_1":dong_name,
                       "area_2":None, 
                       "business": business_name, 
                       "funds" : funds, 
                       "sales_23_2q":int(avg_target_1qb/10000), 
                       "esti_23_3q" : int(estimate_result[0]/10000), 
                        "pred_23_4q" : int(predict_result[0]/10000), 
                        "top_influ" : shapValueOutputTop5, 
                        "bottom_influ" : shapValueOutputBottom5, 
                        "sim_result" : analysis, 
                        "avg_sale_comp" : int(seoul_diff), 
                        "sale_updown":analysis_avg_diff, 
                        "market_active":analysis_active, 
                        "opening_updown":analysis_opening, 
                        "area_growth":analysis_growth, 
                        "fpeople_updown":analysis_mp,
                        "simil_area_name_1": similar_dongs1_name, 
                        "simil_area_esti_1":int(similar_dongs1_pred/10000), 
                        "simil_area_diff_1":int(similar_dongs1_diff[0]/10000), 
                        "simil_area_name_2": similar_dongs2_name, 
                        "simil_area_esti_2":int(similar_dongs2_pred/10000), 
                        "simil_area_diff_2":int(similar_dongs2_diff[0]/10000),
                        "rent_fee": int(franchise[0]/10),
                        "posi_fran_num":franchise[1],
                        "franchise_rec_1": franchise[2],
                        "franchise_rec_2": franchise[3]
                    }

        return Response(output_data, status=status.HTTP_200_OK)



        


    
    
    
# 23 상권
class market_ai(APIView):
    def get(self, request, *args, **kwargs):        
        
        
        # 입력받은 한글 데이터를 디코딩
        goo_name = unquote(self.kwargs['goo'])
        market_name = unquote(self.kwargs['market'])
        business_name = unquote(self.kwargs['business'])
        funds = self.kwargs['funds']
        
        
        # 코드 명을 코드로 변경
        goo = MarketSortedDbFin.objects.filter(자치구_코드_명=goo_name).first().자치구_코드
        market = MarketServiceDataEstimateTestFull.objects.filter(상권_코드_명=market_name).first().상권_코드
        dong_name = MarketServiceDataEstimateTestFull.objects.filter(상권_코드_명=market_name).first().행정동_코드_명

        business = MarketServiceDataEstimateTestFull.objects.filter(서비스_업종_코드_명 = business_name).first().서비스_업종_코드

        # 상권 단위 예측, 추정 feature
        x_cols = ['상권_코드', '서비스_업종_코드', '관공서_수', '은행_수', '종합병원_수', '일반_병원_수', '약국_수',
       '유치원_수', '초등학교_수', '중학교_수', '고등학교_수', '대학교_수', '백화점_수', '슈퍼마켓_수',
       '극장_수', '숙박_시설_수', '공항_수', '철도_역_수', '버스_터미널_수', '지하철_역_수', '버스_정거장_수',
       '연령대_10_직장_인구_수', '연령대_20_직장_인구_수', '연령대_30_직장_인구_수', '연령대_40_직장_인구_수',
       '연령대_50_직장_인구_수', '연령대_60_이상_직장_인구_수', '점포_수', '개업_율', '개업_점포_수',
       '폐업_률', '폐업_점포_수', '프랜차이즈_점포_수', '자치구_코드', '행정동_코드', '아파트_단지_수',
       '아파트_면적_66_제곱미터_미만_세대_수', '아파트_면적_66_제곱미터_세대_수', '아파트_면적_99_제곱미터_세대_수',
       '아파트_면적_132_제곱미터_세대_수', '아파트_면적_165_제곱미터_세대_수', '아파트_가격_1_억_미만_세대_수',
       '아파트_가격_1_억_세대_수', '아파트_가격_2_억_세대_수', '아파트_가격_3_억_세대_수',
       '아파트_가격_4_억_세대_수', '아파트_가격_5_억_세대_수', '아파트_가격_6_억_이상_세대_수', '아파트_평균_면적',
       '아파트_평균_시가', '월_평균_소득_금액', '식료품_지출_총금액', '의류_신발_지출_총금액', '생활용품_지출_총금액',
       '의료비_지출_총금액', '교통_지출_총금액', '여가_지출_총금액', '문화_지출_총금액', '교육_지출_총금액',
       '유흥_지출_총금액', '연령대_10_유동인구_수', '연령대_20_유동인구_수', '연령대_30_유동인구_수',
       '연령대_40_유동인구_수', '연령대_50_유동인구_수', '연령대_60_이상_유동인구_수',
       '시간대_00_06_유동인구_수', '시간대_06_11_유동인구_수', '시간대_11_14_유동인구_수',
       '시간대_14_17_유동인구_수', '시간대_17_21_유동인구_수', '시간대_21_24_유동인구_수',
       '연령대_10_상주인구_수', '연령대_20_상주인구_수', '연령대_30_상주인구_수', '연령대_40_상주인구_수',
       '연령대_50_상주인구_수', '연령대_60_이상_상주인구_수', '아파트_가구_수', '비_아파트_가구_수', '분기',
       '코로나_여부', '주중_평균_유동인구', '주말_평균_유동인구', '전년도_점포별_평균_매출_금액']
        
        # 상권 단위 추정
        queryset_estimate = MarketServiceDataEstimateTestFull.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values(*x_cols)
        queryset_estimate = queryset_estimate[0]
        
        # 상권 단위 예측
        queryset_predict = MarketServiceDataPredictTestFull.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values(*x_cols)
        queryset_predict= queryset_predict[0]
        
        
        # AI 실행, 예측과 추정 수행
        data_pd = pd.DataFrame(queryset_estimate, index=[0])
        
        final_model = load_model("analysis/aimodel/market_service_estimate_model2")
        prediction = predict_model(final_model, data = data_pd)
        estimate_result = prediction['prediction_label']

        data_pd = pd.DataFrame(queryset_predict, index=[0])
        
        final_model = load_model("analysis/aimodel/market_service_pred_model2")
        prediction = predict_model(final_model, data = data_pd)
        predict_result = prediction['prediction_label']
        goo = goo_name
       
        
        
        # shap 값이 있는 지역일 경우 shap 값 로드
        
        try:
            shapValue = MarketServiceEstimateShapValues.objects.filter(상권_코드 = market, 서비스_업종_코드 = business).first()
            
            shapValue = MarketServiceEstimateShapValuesSerializer(shapValue).data
            
            del shapValue['상권_코드']
            del shapValue['서비스_업종_코드']
            
            shapValue = dict(sorted(shapValue.items(), key=lambda item: item[1], reverse=True))

            shapValueOutputTop5 = {}
            count = 0
            for key, item in shapValue.items():
                if item == 0:
                    continue
                shapValueOutputTop5[key] = item
                count += 1
                if count == 5:
                    break

            shapValueOutputBottom5 = {}
            count = 0
            for key, item in reversed(shapValue.items()):
                if item == 0:
                    continue
                shapValueOutputBottom5[key] = item
                count += 1
                if count == 5:
                    break
                
        except:
            
            # 없을 경우 shap 값은 None
            shapValueOutputTop5 = None
            shapValueOutputBottom5 = None
            
            
        # 가장 영향력이 높은 긍정적, 부정적 요소들을 5개 씩 shap 값으로 선정
        shapValueOutputTop5 = {key: int(value) for key, value in shapValueOutputTop5.items()}
        shapValueOutputBottom5 = {key: int(value) for key, value in shapValueOutputBottom5.items()}
            
        
        # 기준 년분기의 서울시 내 동일 업종의 점포별 평균 매출 금액으로 창업지수 계산
        queryset_avg_seoul = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business).values("점포별_평균_매출_금액")
        avg_zero = 0
        count = 0
        for i in queryset_avg_seoul:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        seoul_avg = avg_zero/count
        
        seoul_diff = (estimate_result.values/seoul_avg)*100
        
        
        if seoul_diff > 150:
            analysis = "양호"
        
        elif seoul_diff < 50:
            analysis = "위험"
        else:
            analysis = "보통"
        
        if seoul_diff > 200:
            seoul_diff = 200
        
        jachigu = MarketSortedDbFin.objects.filter(상권_코드 = market).values('자치구_코드', '자치구_코드_명').first()

        # 해당 상권 1, 2 분기 점포별 평균 매출 금액을 활용 AI리포트 내용 생성
        # 지역별 활성화 여부      
        queryset_avg_1qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business, 자치구_코드 = jachigu['자치구_코드']).values("점포별_평균_매출_금액")
        queryset_avg_2qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20231, 서비스_업종_코드 = business, 자치구_코드 = jachigu['자치구_코드']).values("점포별_평균_매출_금액")

        avg_zero = 0
        count = 0
        for i in queryset_avg_1qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_1qb = avg_zero/count    
        
        
        
        avg_zero = 0
        count = 0
        for i in queryset_avg_2qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_2qb = avg_zero/count   

        analysis_avg_diff = "증가" if (avg_2qb - avg_1qb) > 0 else "감소"
        analysis_active = "활성화" if (avg_2qb - avg_1qb) > 0 else "비활성화"
        
        
         # 작년 동분기와 현재의 창업 수 비교 발달, 쇠퇴 여부 표시
        queryset_opening = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values('점포_수')
        opening = queryset_opening[0]['점포_수']
        
        queryset_opening_lyb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 상권_코드 = market, 서비스_업종_코드 = business).values('점포_수')
        opening_lyb = queryset_opening_lyb[0]['점포_수']
        
        
        analysis_opening = "증가" if (opening - opening_lyb) > 0 else "감소"
        analysis_growth = "발달" if (opening - opening_lyb) > 0 else "쇠퇴"
        
        # 작년 동분기와 현재의 유동인구 수 비교
        queryset_mp_1yb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 상권_코드 = market, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp_1yb = queryset_mp_1yb[0]['총_유동인구_수']
        
        queryset_mp = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp = queryset_mp[0]['총_유동인구_수']
        
        
        analysis_mp = "증가" if (mp - mp_1yb) > 0 else "감소"
        
        
        # 매출이 비슷한 주변 지역 두 곳 선정
        queryset_similar = MarketServiceEstimateY.objects.filter(서비스_업종_코드 = business).values('상권_코드', 'prediction_label') 
        
        for i in queryset_similar:
            num = i['prediction_label']
            diff = abs(num - estimate_result.values)
            i['diff'] = diff
            
        sortedList = sorted(queryset_similar, key=lambda x: x['diff'], reverse=True)
        num1 = sortedList[0]
        num2 = sortedList[1]
        
        similar_market1 = MarketSortedDbFin.objects.filter(상권_코드 = num1['상권_코드']).values('상권_코드_명').first()
        similar_market2 = MarketSortedDbFin.objects.filter(상권_코드 = num2['상권_코드']).values('상권_코드_명').first()
        
        similar_market1_name = similar_market1['상권_코드_명']
        similar_market1_pred = num1['prediction_label']
        similar_market1_diff = estimate_result.values - similar_market1_pred
        
        similar_market2_name = similar_market2['상권_코드_명']
        similar_market2_pred = num2['prediction_label']
        similar_market2_diff = estimate_result.values - similar_market2_pred
        
        
        queryset_target_avg_1qb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business, 상권_코드 = market).values("점포별_평균_매출_금액")
        
        avg_zero = 0
        count = 0
        for i in queryset_target_avg_1qb:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        avg_target_1qb = avg_zero/count  
        
        # 자본금 기준 프랜차이즈 추천
        franchise = get_franchise_data_dong(dong_name, business_name, funds)

        
        # 프랜차이즈 비용 int화 및 단위 통일
        if franchise[2] != None:
            franchise[2] = {key: int(int(value) / 10) if key != '브랜드명' else value for key, value in franchise[2].items()}
        if franchise[3] != None:
            franchise[3] = {key: int(int(value) / 10) if key != '브랜드명' else value for key, value in franchise[3].items()}
        
        # 10000원 단위로 바꿔 리포트 데이터 전달
        output_data = {
                "AI": "상권",
                "region": goo,
                "area_1": market_name,
                "area_2": dong_name,
                "business": business_name,
                "funds": funds,
                "sales_23_2q": int(avg_target_1qb/10000),
                "esti_23_3q": int(estimate_result[0]/10000),
                "pred_23_4q": int(predict_result[0]/10000),
                "top_influ": shapValueOutputTop5,
                "bottom_influ": shapValueOutputBottom5,
                "sim_result": analysis,
                "avg_sale_comp": int(seoul_diff),
                "sale_updown": analysis_avg_diff,
                "market_active": analysis_active,
                "opening_updown": analysis_opening,
                "area_growth": analysis_growth,
                "fpeople_updown": analysis_mp,
                "simil_area_name_1": similar_market1_name,
                "simil_area_esti_1": int(similar_market1_pred/10000),
                "simil_area_diff_1": int(similar_market1_diff[0]/10000),
                "simil_area_name_2": similar_market2_name,
                "simil_area_esti_2": int(similar_market2_pred/10000),
                "simil_area_diff_2": int(similar_market2_diff/10000),
                "rent_fee": int(franchise[0]/10),
                "posi_fran_num":franchise[1],
                "franchise_rec_1": franchise[2],
                "franchise_rec_2": franchise[3]
            }
 
        return Response(output_data, status=status.HTTP_200_OK)

        
def rent_cost_data(name_dong):
        rent_cost_last_data =1
        
        queryset_estimate = SeoulRent.objects.filter(dong_name=name_dong).values("area_name")
        
        vacancy_data = ["임대료","평균임대면적"]

        area_name = len(queryset_estimate)

        #임대료 데이터가 존재하거나 하나일 경우
        if len(queryset_estimate) == 1 :
            # temp_data = vacancyrate 상세지역
            temp_data = queryset_estimate[0]["area_name"]
            
            # temp = "" 이면 임대료 정보 x
            if temp_data != "":
                rent_cost = Vacancyrate.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data = rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
            else :
                rent_cost_last_data = -1
        
        # 임대료 데이터가 중복일 경우
        else :
            rent_cost_last_data = len(queryset_estimate) 
    
             
            for i in range(len(queryset_estimate) ):
                temp_data = queryset_estimate[i]["area_name"]
                rent_cost = Vacancyrate.objects.filter(상세지역 = temp_data).values(*vacancy_data)
                rent_cost_last_data += rent_cost[0]["임대료"] * rent_cost[0]["평균임대면적"]
                print(rent_cost_last_data)

            rent_cost_last_data = rent_cost_last_data / len(queryset_estimate) 
        
        return rent_cost_last_data
           
    
    

