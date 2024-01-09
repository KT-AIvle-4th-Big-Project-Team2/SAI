
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


# 행정동

class dong_ai(generics.GenericAPIView):
    serializer_class = AIReportSerializer
    
    def post(self, request, *args, **kargs):
    
        goo = self.kwargs['goo'].upper()
        dong = self.kwargs['dong'].upper()
        business = self.kwargs['business'].upper()
        funds = self.kwargs['funds']
        
        goo_name = MarketSortedDbFin.objects.filter(자치구_코드=goo).first().자치구_코드_명
        
        dong_name = DongServiceDataEstimateTestFullFin.objects.filter(행정동_코드=dong).first().행정동_코드_명
        
        business_name = DongServiceDataEstimateTestFullFin.objects.filter(서비스_업종_코드 = business).first().서비스_업종_코드_명

        
        
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
        
        try:
            shapValue = DongServiceEstimateShapValues.objects.filter(행정동_코드 = dong, 서비스_업종_코드 = business).first()
            shapValue = DongServiceEstimateShapValuesSerializer(shapValue).data
            del shapValue['행정동_코드']
            del shapValue['서비스_업종_코드']
            
            # shapValue = dict(sorted(shapValue.items(), key=lambda item: abs(item[1]), reverse=True))

            # shapValueOutputTop5 = {}
            # count = 0
            # for key, item in shapValue.items():
            #     shapValueOutputTop5[key] = int(item)
            #     count += 1
            #     if count == 5:break
            
            
            # shapValueOutputBottom5 = {}
            # count = 0
            # for key, item in reversed(shapValue.items()):
            #     if int(item) == 0:
            #         pass
            #     else:
            #         shapValueOutputBottom5[key] = int(item)
            #         count += 1
            #         if count == 5:break
            
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
            shapValueOutputTop5 = None
            shapValueOutputBottom5 = None    
        goo = goo_name
        queryset_avg_seoul = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business).values("점포별_평균_매출_금액")
        avg_zero = 0
        count = 0
        for i in queryset_avg_seoul:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        seoul_avg = avg_zero/count
        
        seoul_diff = (estimate_result.values/seoul_avg)*100
        
        
        jachigu = MarketSortedDbFin.objects.filter(행정동_코드 = dong).values('자치구_코드', '자치구_코드_명').first()
        
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
        
        queryset_opening = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values('점포_수')
        opening = queryset_opening[0]['점포_수']
        
        queryset_opening_lyb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 행정동_코드 = dong, 서비스_업종_코드 = business).values('점포_수')
        opening_lyb = queryset_opening_lyb[0]['점포_수']
        
        
        analysis_opening = "증가" if (opening - opening_lyb) > 0 else "감소"
        analysis_growth = "발달" if (opening - opening_lyb) > 0 else "쇠퇴"
        
        
        queryset_mp_1yb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 행정동_코드 = dong, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp_1yb = queryset_mp_1yb[0]['총_유동인구_수']
        
        queryset_mp = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 행정동_코드 = dong, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp = queryset_mp[0]['총_유동인구_수']
        
        
        analysis_mp = "증가" if (mp - mp_1yb) > 0 else "감소"
        
        
        if seoul_diff >= 80:
            analysis = "양호"
        
        elif seoul_diff <= 20:
            analysis = "위험"
        else:
            analysis = "보통"
        
        queryset_similar = DongServiceEstimateY.objects.filter(서비스_업종_코드 = business).values('행정동_코드', 'prediction_label') # 4분기?
        
        #difference = [float('inf'), float('inf')]
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
        
        output_data = {"AI":"행정동",
                       "region":goo, 
                       "area":dong_name, 
                       "business": business_name, 
                       "funds" : funds, 
                       "sales_23_2q":int(avg_target_1qb), 
                       "esti_23_3q" : int(estimate_result[0]), 
                        "pred_23_4q" : int(predict_result[0]), 
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
                        "simil_area_esti_1":int(similar_dongs1_pred), 
                        "simil_area_diff_1":int(similar_dongs1_diff[0]), 
                        "simil_area_name_2": similar_dongs2_name, 
                        "simil_area_esti_2":int(similar_dongs2_pred), 
                        "simil_area_diff_2":int(similar_dongs2_diff[0])
                    }

        username = self.request.data.get("username")
        user_id = UserCustom.objects.get(username = username).user_id
        
        save_data = output_data
        save_data["user"] = user_id
        
        serialised = AIReportSerializer(data = save_data)
        if serialised.is_valid(): serialised.save()
        else: return Response({"report save failed" : serialised.errors}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(output_data, status=status.HTTP_200_OK)



        


    
    
    
# 23년 상권 예상
class market_ai(APIView):
    def post(self, request, *args, **kargs):        
        goo = self.kwargs['goo'].upper()
        market = self.kwargs['market']
        business = self.kwargs['business'].upper()
        funds = self.kwargs['funds']
        goo_name = MarketSortedDbFin.objects.filter(자치구_코드=goo).first().자치구_코드_명
        market_name = MarketServiceDataEstimateTestFull.objects.filter(상권_코드=market).first().상권_코드_명
        
        business_name = MarketServiceDataEstimateTestFull.objects.filter(서비스_업종_코드 = business).first().서비스_업종_코드_명
    
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
        
        
        queryset_estimate = MarketServiceDataEstimateTestFull.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values(*x_cols)
        queryset_estimate = queryset_estimate[0]
        
        queryset_predict = MarketServiceDataPredictTestFull.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values(*x_cols)
        queryset_predict= queryset_predict[0]
        
        
        
        data_pd = pd.DataFrame(queryset_estimate, index=[0])
        
        final_model = load_model("analysis/aimodel/market_service_estimate_model2")
        prediction = predict_model(final_model, data = data_pd)
        estimate_result = prediction['prediction_label']

        data_pd = pd.DataFrame(queryset_predict, index=[0])
        
        final_model = load_model("analysis/aimodel/market_service_pred_model2")
        prediction = predict_model(final_model, data = data_pd)
        predict_result = prediction['prediction_label']
        goo = goo_name
       
        
        try:
            shapValue = MarketServiceEstimateShapValues.objects.filter(상권_코드 = market, 서비스_업종_코드 = business).first()
            
            shapValue = MarketServiceEstimateShapValuesSerializer(shapValue).data
            
            del shapValue['상권_코드']
            del shapValue['서비스_업종_코드']

            # shapValue = dict(sorted(shapValue.items(), reverse=True))

            
            
            #dict(sorted(shapValue.items(), key=lambda item: item[1], reverse=True)[:5])
            #dict(sorted(shapValue.items(), key=lambda item: item[1])[:5])
            
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
            
            # shapValueOutputTop5 = {} 
            # count = 0
            # for key, item in shapValue.items():
            #     shapValueOutputTop5[key] = int(item)
            #     count += 1
            #     if count == 5:break
            
            
            # shapValueOutputBottom5 = {} #
            # count = 0
            # for key, item in reversed(shapValue.items()):
            #     if int(item) == 0:
            #         pass
            #     else:
            #         shapValueOutputBottom5[key] = int(item)
            #         count += 1
            #         if count == 5:break
        except:
            shapValueOutputTop5 = None
            shapValueOutputBottom5 = None
        queryset_avg_seoul = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20232, 서비스_업종_코드 = business).values("점포별_평균_매출_금액")
        avg_zero = 0
        count = 0
        for i in queryset_avg_seoul:
            avg_zero += i['점포별_평균_매출_금액']
            count += 1
        seoul_avg = avg_zero/count
        
        seoul_diff = (estimate_result.values/seoul_avg)*100
        
        
        jachigu = MarketSortedDbFin.objects.filter(상권_코드 = market).values('자치구_코드', '자치구_코드_명').first()


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
        
        queryset_opening = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values('점포_수')
        opening = queryset_opening[0]['점포_수']
        
        queryset_opening_lyb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 상권_코드 = market, 서비스_업종_코드 = business).values('점포_수')
        opening_lyb = queryset_opening_lyb[0]['점포_수']
        
        
        analysis_opening = "증가" if (opening - opening_lyb) > 0 else "감소"
        analysis_growth = "발달" if (opening - opening_lyb) > 0 else "쇠퇴"
        
        
        queryset_mp_1yb = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20223, 상권_코드 = market, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp_1yb = queryset_mp_1yb[0]['총_유동인구_수']
        
        queryset_mp = MarketSortedDbFin.objects.filter(기준_년분기_코드 = 20233, 상권_코드 = market, 서비스_업종_코드 = business).values('총_유동인구_수')
        mp = queryset_mp[0]['총_유동인구_수']
        
        
        analysis_mp = "증가" if (mp - mp_1yb) > 0 else "감소"
        
        
        if seoul_diff > 80:
            analysis = "양호"
        
        elif seoul_diff < 20:
            analysis = "위험"
        else:
            analysis = "보통"
        
        queryset_similar = MarketServiceEstimateY.objects.filter(서비스_업종_코드 = business).values('상권_코드', 'prediction_label') # 4분기?
        
        
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
        
        output_data = {
                "AI": "상권",
                "region": goo,
                "area": market_name,
                "business": business_name,
                "funds": funds,
                "sales_23_2q": int(avg_target_1qb),
                "esti_23_3q": int(estimate_result[0]),
                "pred_23_4q": int(predict_result[0]),
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
                "simil_area_esti_1": int(similar_market1_pred),
                "simil_area_diff_1": int(similar_market1_diff[0]),
                "simil_area_name_2": similar_market2_name,
                "simil_area_esti_2": int(similar_market2_pred),
                "simil_area_diff_2": int(similar_market2_diff)
            }
                
        username = self.request.data.get("username")
        user_id = UserCustom.objects.get(username = username).user_id
        
        save_data = output_data
        save_data["user"] = user_id
        serialised = AIReportSerializer(data = save_data)
        if serialised.is_valid(): serialised.save()
        else: return Response({"report save failed" : serialised.errors}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(output_data, status=status.HTTP_200_OK)
    

class AIReportListView(APIView):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        
        instance = AiReport.objects.filter(user__username = username).values(
            "report_id",
            "region",
            "area",
            "business",
            "funds",
            "sim_result",
            "creationdate"
        )

        
        return Response(instance, status.HTTP_400_BAD_REQUEST)
    
class AIReportView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        report_id = kwargs['num']
        username = request.data.get("username")
        
        try:
            queryset = AiReport.objects.get(report_id = report_id)
        except:
            return Response({'no matching report found'}, status.HTTP_404_NOT_FOUND)
             
        if queryset.user.username != username: raise ValidationError({'wrong user no auth'}, status.HTTP_401_UNAUTHORIZED)
        
        serializer = AIReportSerializer(queryset)
       
        serializer.data
        
        return Response(serializer.data, status.HTTP_200_OK)
class AIReportDeleteView(APIView):
    
    def delete(self, request, *args, **kwargs):
        
        report_id = kwargs['num']
        username = request.data.get("username")
        
        try:
            queryset = AiReport.objects.get(report_id = report_id)
        except:
            return Response({'no matching report found'}, status.HTTP_404_NOT_FOUND)
             
        if queryset.user.username != username: raise ValidationError({'wrong user no auth'}, status.HTTP_401_UNAUTHORIZED)
        
        queryset.delete()
        
        return Response('Report deleted', status.HTTP_200_OK)
    
    
    
