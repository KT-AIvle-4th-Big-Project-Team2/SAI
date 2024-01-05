# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MarketData(models.Model):
    기준_년분기_코드 = models.IntegerField(blank=True, null=True)
    상권_구분_코드 = models.TextField(blank=True, null=True)
    상권_구분_코드_명 = models.TextField(blank=True, null=True)
    상권_코드 = models.IntegerField(blank=True, null=True)
    상권_코드_명 = models.TextField(blank=True, null=True)
    서비스_업종_코드 = models.TextField(blank=True, null=True)
    서비스_업종_코드_명 = models.TextField(blank=True, null=True)
    당월_매출_금액 = models.FloatField(blank=True, null=True)
    당월_매출_건수 = models.IntegerField(blank=True, null=True)
    주중_매출_금액 = models.FloatField(blank=True, null=True)
    주말_매출_금액 = models.FloatField(blank=True, null=True)
    월요일_매출_금액 = models.IntegerField(blank=True, null=True)
    화요일_매출_금액 = models.FloatField(blank=True, null=True)
    수요일_매출_금액 = models.FloatField(blank=True, null=True)
    목요일_매출_금액 = models.FloatField(blank=True, null=True)
    금요일_매출_금액 = models.FloatField(blank=True, null=True)
    토요일_매출_금액 = models.IntegerField(blank=True, null=True)
    일요일_매출_금액 = models.IntegerField(blank=True, null=True)
    시간대_00_06_매출_금액 = models.IntegerField(db_column='시간대_00~06_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_06_11_매출_금액 = models.IntegerField(db_column='시간대_06~11_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_11_14_매출_금액 = models.FloatField(db_column='시간대_11~14_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_14_17_매출_금액 = models.IntegerField(db_column='시간대_14~17_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_17_21_매출_금액 = models.FloatField(db_column='시간대_17~21_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_21_24_매출_금액 = models.FloatField(db_column='시간대_21~24_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    남성_매출_금액 = models.FloatField(blank=True, null=True)
    여성_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_10_매출_금액 = models.IntegerField(blank=True, null=True)
    연령대_20_매출_금액 = models.IntegerField(blank=True, null=True)
    연령대_30_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_40_매출_금액 = models.IntegerField(blank=True, null=True)
    연령대_50_매출_금액 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_매출_금액 = models.IntegerField(blank=True, null=True)
    주중_매출_건수 = models.IntegerField(blank=True, null=True)
    주말_매출_건수 = models.IntegerField(blank=True, null=True)
    월요일_매출_건수 = models.IntegerField(blank=True, null=True)
    화요일_매출_건수 = models.IntegerField(blank=True, null=True)
    수요일_매출_건수 = models.IntegerField(blank=True, null=True)
    목요일_매출_건수 = models.IntegerField(blank=True, null=True)
    금요일_매출_건수 = models.IntegerField(blank=True, null=True)
    토요일_매출_건수 = models.IntegerField(blank=True, null=True)
    일요일_매출_건수 = models.IntegerField(blank=True, null=True)
    시간대_건수_06_매출_건수 = models.IntegerField(db_column='시간대_건수~06_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_11_매출_건수 = models.IntegerField(db_column='시간대_건수~11_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_14_매출_건수 = models.IntegerField(db_column='시간대_건수~14_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_17_매출_건수 = models.IntegerField(db_column='시간대_건수~17_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_21_매출_건수 = models.IntegerField(db_column='시간대_건수~21_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_24_매출_건수 = models.IntegerField(db_column='시간대_건수~24_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    남성_매출_건수 = models.IntegerField(blank=True, null=True)
    여성_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_10_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_20_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_30_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_40_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_50_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_매출_건수 = models.IntegerField(blank=True, null=True)
    집객시설_수 = models.FloatField(blank=True, null=True)
    관공서_수 = models.FloatField(blank=True, null=True)
    은행_수 = models.FloatField(blank=True, null=True)
    종합병원_수 = models.FloatField(blank=True, null=True)
    일반_병원_수 = models.FloatField(blank=True, null=True)
    약국_수 = models.FloatField(blank=True, null=True)
    유치원_수 = models.FloatField(blank=True, null=True)
    초등학교_수 = models.FloatField(blank=True, null=True)
    중학교_수 = models.FloatField(blank=True, null=True)
    고등학교_수 = models.FloatField(blank=True, null=True)
    대학교_수 = models.FloatField(blank=True, null=True)
    백화점_수 = models.FloatField(blank=True, null=True)
    슈퍼마켓_수 = models.FloatField(blank=True, null=True)
    극장_수 = models.FloatField(blank=True, null=True)
    숙박_시설_수 = models.FloatField(blank=True, null=True)
    공항_수 = models.FloatField(blank=True, null=True)
    철도_역_수 = models.FloatField(blank=True, null=True)
    버스_터미널_수 = models.FloatField(blank=True, null=True)
    지하철_역_수 = models.FloatField(blank=True, null=True)
    버스_정거장_수 = models.FloatField(blank=True, null=True)
    총_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_10_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_20_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_30_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_40_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_50_직장_인구_수 = models.FloatField(blank=True, null=True)
    연령대_60_이상_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_10_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_20_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_30_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_40_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_50_직장_인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_60_이상_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_10_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_20_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_30_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_40_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_50_직장_인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_60_이상_직장_인구_수 = models.FloatField(blank=True, null=True)
    점포_수 = models.IntegerField(blank=True, null=True)
    유사_업종_점포_수 = models.IntegerField(blank=True, null=True)
    개업_율 = models.IntegerField(blank=True, null=True)
    개업_점포_수 = models.IntegerField(blank=True, null=True)
    폐업_률 = models.IntegerField(blank=True, null=True)
    폐업_점포_수 = models.IntegerField(blank=True, null=True)
    프랜차이즈_점포_수 = models.IntegerField(blank=True, null=True)
    엑스좌표_값 = models.IntegerField(blank=True, null=True)
    와이좌표_값 = models.IntegerField(blank=True, null=True)
    자치구_코드 = models.IntegerField(blank=True, null=True)
    자치구_코드_명 = models.TextField(blank=True, null=True)
    행정동_코드 = models.IntegerField(blank=True, null=True)
    행정동_코드_명 = models.TextField(blank=True, null=True)
    영역_면적 = models.IntegerField(blank=True, null=True)
    아파트_단지_수 = models.FloatField(blank=True, null=True)
    아파트_면적_66_제곱미터_미만_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_66_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_99_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_132_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_165_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_1_억_미만_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_1_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_2_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_3_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_4_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_5_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_6_억_이상_세대_수 = models.FloatField(blank=True, null=True)
    아파트_평균_면적 = models.FloatField(blank=True, null=True)
    아파트_평균_시가 = models.FloatField(blank=True, null=True)
    월_평균_소득_금액 = models.FloatField(blank=True, null=True)
    소득_구간_코드 = models.FloatField(blank=True, null=True)
    지출_총금액 = models.FloatField(blank=True, null=True)
    식료품_지출_총금액 = models.FloatField(blank=True, null=True)
    의류_신발_지출_총금액 = models.FloatField(blank=True, null=True)
    생활용품_지출_총금액 = models.FloatField(blank=True, null=True)
    의료비_지출_총금액 = models.FloatField(blank=True, null=True)
    교통_지출_총금액 = models.FloatField(blank=True, null=True)
    여가_지출_총금액 = models.FloatField(blank=True, null=True)
    문화_지출_총금액 = models.FloatField(blank=True, null=True)
    교육_지출_총금액 = models.FloatField(blank=True, null=True)
    유흥_지출_총금액 = models.FloatField(blank=True, null=True)
    총_유동인구_수 = models.IntegerField(blank=True, null=True)
    남성_유동인구_수 = models.IntegerField(blank=True, null=True)
    여성_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_10_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_20_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_30_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_40_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_50_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_00_06_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_06_11_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_11_14_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_14_17_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_17_21_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_21_24_유동인구_수 = models.IntegerField(blank=True, null=True)
    월요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    화요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    수요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    목요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    금요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    토요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    일요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    총_상주인구_수 = models.FloatField(blank=True, null=True)
    남성_상주인구_수 = models.FloatField(blank=True, null=True)
    여성_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_10_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_20_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_30_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_40_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_50_상주인구_수 = models.FloatField(blank=True, null=True)
    연령대_60_이상_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_10_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_20_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_30_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_40_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_50_상주인구_수 = models.FloatField(blank=True, null=True)
    남성연령대_60_이상_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_10_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_20_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_30_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_40_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_50_상주인구_수 = models.FloatField(blank=True, null=True)
    여성연령대_60_이상_상주인구_수 = models.FloatField(blank=True, null=True)
    총_가구_수 = models.FloatField(blank=True, null=True)
    아파트_가구_수 = models.FloatField(blank=True, null=True)
    비_아파트_가구_수 = models.FloatField(blank=True, null=True)
    점포별_평균_매출_금액 = models.FloatField(blank=True, null=True)
    분기 = models.IntegerField(blank=True, null=True)
    코로나_여부 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_data'


class Franchise(models.Model):
    indutylclasnm_x = models.CharField(db_column='indutyLclasNm_x', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indutymlsfcnm_x = models.CharField(db_column='indutyMlsfcNm_x', max_length=50, blank=True, null=True)  # Field name made lowercase.
    corpnm_x = models.CharField(db_column='corpNm_x', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brandnm = models.CharField(db_column='brandNm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frcscnt = models.IntegerField(db_column='frcsCnt', blank=True, null=True)  # Field name made lowercase.
    newfrcsrgscnt = models.IntegerField(db_column='newFrcsRgsCnt', blank=True, null=True)  # Field name made lowercase.
    ctrtendcnt = models.IntegerField(db_column='ctrtEndCnt', blank=True, null=True)  # Field name made lowercase.
    ctrtcncltncnt = models.IntegerField(db_column='ctrtCncltnCnt', blank=True, null=True)  # Field name made lowercase.
    nmchgcnt = models.IntegerField(db_column='nmChgCnt', blank=True, null=True)  # Field name made lowercase.
    avrgslsamt = models.IntegerField(db_column='avrgSlsAmt', blank=True, null=True)  # Field name made lowercase.
    arunitavrgslsamt = models.IntegerField(db_column='arUnitAvrgSlsAmt', blank=True, null=True)  # Field name made lowercase.
    indutylclasnm_y = models.CharField(db_column='indutyLclasNm_y', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indutymlsfcnm_y = models.CharField(db_column='indutyMlsfcNm_y', max_length=50, blank=True, null=True)  # Field name made lowercase.
    corpnm_y = models.CharField(db_column='corpNm_y', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jngbzmnjngamt = models.IntegerField(db_column='jngBzmnJngAmt', blank=True, null=True)  # Field name made lowercase.
    jngbzmneduamt = models.IntegerField(db_column='jngBzmnEduAmt', blank=True, null=True)  # Field name made lowercase.
    jngbzmnassrncamt = models.IntegerField(db_column='jngBzmnAssrncAmt', blank=True, null=True)  # Field name made lowercase.
    jngbzmnetcamt = models.IntegerField(db_column='jngBzmnEtcAmt', blank=True, null=True)  # Field name made lowercase.
    smtnamt = models.IntegerField(db_column='smtnAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Franchise'


class SeoulRent(models.Model):
    dong_code = models.IntegerField(blank=True, null=True)
    dong_name = models.TextField(blank=True, null=True)
    area_size = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latituded = models.FloatField(blank=True, null=True)
    area_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul_rent'


class Vacancyrate(models.Model):
    지역별 = models.TextField(blank=True, null=True)
    상세_지역 = models.TextField(db_column='상세 지역', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    임대료_천원_field = models.FloatField(db_column='임대료(천원/㎡)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    평균_임대_면적_field = models.FloatField(db_column='평균 임대 면적(㎡)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'vacancyrate'


class AiReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    estimate_sales = models.IntegerField()
    predict_sales = models.IntegerField()
    creationdate = models.DateTimeField()
    user = models.ForeignKey('AccountUsercustom', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ai_report'


class DongData(models.Model):
    기준_년분기_코드 = models.IntegerField(blank=True, null=True)
    행정동_코드 = models.IntegerField(blank=True, null=True)
    행정동_코드_명 = models.TextField(blank=True, null=True)
    서비스_업종_코드 = models.TextField(blank=True, null=True)
    서비스_업종_코드_명 = models.TextField(blank=True, null=True)
    당월_매출_금액 = models.FloatField(blank=True, null=True)
    당월_매출_건수 = models.FloatField(blank=True, null=True)
    주중_매출_금액 = models.FloatField(blank=True, null=True)
    주말_매출_금액 = models.FloatField(blank=True, null=True)
    월요일_매출_금액 = models.FloatField(blank=True, null=True)
    화요일_매출_금액 = models.FloatField(blank=True, null=True)
    수요일_매출_금액 = models.FloatField(blank=True, null=True)
    목요일_매출_금액 = models.FloatField(blank=True, null=True)
    금요일_매출_금액 = models.FloatField(blank=True, null=True)
    토요일_매출_금액 = models.FloatField(blank=True, null=True)
    일요일_매출_금액 = models.FloatField(blank=True, null=True)
    시간대_00_06_매출_금액 = models.FloatField(db_column='시간대_00~06_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_06_11_매출_금액 = models.FloatField(db_column='시간대_06~11_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_11_14_매출_금액 = models.FloatField(db_column='시간대_11~14_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_14_17_매출_금액 = models.FloatField(db_column='시간대_14~17_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_17_21_매출_금액 = models.FloatField(db_column='시간대_17~21_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_21_24_매출_금액 = models.FloatField(db_column='시간대_21~24_매출_금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    남성_매출_금액 = models.FloatField(blank=True, null=True)
    여성_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_10_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_20_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_30_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_40_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_50_매출_금액 = models.FloatField(blank=True, null=True)
    연령대_60_이상_매출_금액 = models.FloatField(blank=True, null=True)
    주중_매출_건수 = models.IntegerField(blank=True, null=True)
    주말_매출_건수 = models.IntegerField(blank=True, null=True)
    월요일_매출_건수 = models.IntegerField(blank=True, null=True)
    화요일_매출_건수 = models.IntegerField(blank=True, null=True)
    수요일_매출_건수 = models.IntegerField(blank=True, null=True)
    목요일_매출_건수 = models.IntegerField(blank=True, null=True)
    금요일_매출_건수 = models.IntegerField(blank=True, null=True)
    토요일_매출_건수 = models.IntegerField(blank=True, null=True)
    일요일_매출_건수 = models.IntegerField(blank=True, null=True)
    시간대_건수_06_매출_건수 = models.IntegerField(db_column='시간대_건수~06_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_11_매출_건수 = models.IntegerField(db_column='시간대_건수~11_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_14_매출_건수 = models.IntegerField(db_column='시간대_건수~14_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_17_매출_건수 = models.IntegerField(db_column='시간대_건수~17_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_21_매출_건수 = models.IntegerField(db_column='시간대_건수~21_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    시간대_건수_24_매출_건수 = models.IntegerField(db_column='시간대_건수~24_매출_건수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    남성_매출_건수 = models.IntegerField(blank=True, null=True)
    여성_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_10_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_20_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_30_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_40_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_50_매출_건수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_매출_건수 = models.IntegerField(blank=True, null=True)
    집객시설_수 = models.FloatField(blank=True, null=True)
    관공서_수 = models.FloatField(blank=True, null=True)
    은행_수 = models.FloatField(blank=True, null=True)
    종합병원_수 = models.FloatField(blank=True, null=True)
    일반_병원_수 = models.FloatField(blank=True, null=True)
    약국_수 = models.FloatField(blank=True, null=True)
    유치원_수 = models.FloatField(blank=True, null=True)
    초등학교_수 = models.FloatField(blank=True, null=True)
    중학교_수 = models.FloatField(blank=True, null=True)
    고등학교_수 = models.FloatField(blank=True, null=True)
    대학교_수 = models.FloatField(blank=True, null=True)
    백화점_수 = models.FloatField(blank=True, null=True)
    슈퍼마켓_수 = models.FloatField(blank=True, null=True)
    극장_수 = models.FloatField(blank=True, null=True)
    숙박_시설_수 = models.FloatField(blank=True, null=True)
    공항_수 = models.FloatField(blank=True, null=True)
    철도_역_수 = models.FloatField(blank=True, null=True)
    버스_터미널_수 = models.FloatField(blank=True, null=True)
    지하철_역_수 = models.FloatField(blank=True, null=True)
    버스_정거장_수 = models.FloatField(blank=True, null=True)
    총_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_10_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_20_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_30_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_40_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_50_직장_인구_수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_10_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_20_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_30_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_40_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_50_직장_인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_60_이상_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_10_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_20_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_30_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_40_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_50_직장_인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_60_이상_직장_인구_수 = models.IntegerField(blank=True, null=True)
    점포_수 = models.IntegerField(blank=True, null=True)
    유사_업종_점포_수 = models.IntegerField(blank=True, null=True)
    개업_율 = models.IntegerField(blank=True, null=True)
    개업_점포_수 = models.IntegerField(blank=True, null=True)
    폐업_률 = models.IntegerField(blank=True, null=True)
    폐업_점포_수 = models.IntegerField(blank=True, null=True)
    프랜차이즈_점포_수 = models.IntegerField(blank=True, null=True)
    아파트_단지_수 = models.IntegerField(blank=True, null=True)
    아파트_면적_66_제곱미터_미만_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_66_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_99_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_132_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_면적_165_제곱미터_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_1_억_미만_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_1_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_2_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_3_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_4_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_5_억_세대_수 = models.FloatField(blank=True, null=True)
    아파트_가격_6_억_이상_세대_수 = models.FloatField(blank=True, null=True)
    아파트_평균_면적 = models.IntegerField(blank=True, null=True)
    아파트_평균_시가 = models.FloatField(blank=True, null=True)
    월_평균_소득_금액 = models.FloatField(blank=True, null=True)
    소득_구간_코드 = models.IntegerField(blank=True, null=True)
    지출_총금액 = models.FloatField(blank=True, null=True)
    식료품_지출_총금액 = models.FloatField(blank=True, null=True)
    의류_신발_지출_총금액 = models.FloatField(blank=True, null=True)
    생활용품_지출_총금액 = models.FloatField(blank=True, null=True)
    의료비_지출_총금액 = models.FloatField(blank=True, null=True)
    교통_지출_총금액 = models.FloatField(blank=True, null=True)
    교육_지출_총금액 = models.FloatField(blank=True, null=True)
    유흥_지출_총금액 = models.FloatField(blank=True, null=True)
    여가_문화_지출_총금액 = models.FloatField(blank=True, null=True)
    기타_지출_총금액 = models.FloatField(blank=True, null=True)
    음식_지출_총금액 = models.FloatField(blank=True, null=True)
    총_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_10_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_20_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_30_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_40_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_50_상주인구_수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_10_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_20_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_30_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_40_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_50_상주인구_수 = models.IntegerField(blank=True, null=True)
    남성연령대_60_이상_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_10_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_20_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_30_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_40_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_50_상주인구_수 = models.IntegerField(blank=True, null=True)
    여성연령대_60_이상_상주인구_수 = models.IntegerField(blank=True, null=True)
    총_가구_수 = models.IntegerField(blank=True, null=True)
    아파트_가구_수 = models.IntegerField(blank=True, null=True)
    비_아파트_가구_수 = models.IntegerField(blank=True, null=True)
    총_유동인구_수 = models.IntegerField(blank=True, null=True)
    남성_유동인구_수 = models.IntegerField(blank=True, null=True)
    여성_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_10_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_20_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_30_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_40_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_50_유동인구_수 = models.IntegerField(blank=True, null=True)
    연령대_60_이상_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_00_06_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_06_11_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_11_14_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_14_17_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_17_21_유동인구_수 = models.IntegerField(blank=True, null=True)
    시간대_21_24_유동인구_수 = models.IntegerField(blank=True, null=True)
    월요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    화요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    수요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    목요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    금요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    토요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    일요일_유동인구_수 = models.IntegerField(blank=True, null=True)
    점포별_평균_매출_금액 = models.FloatField(blank=True, null=True)
    분기 = models.IntegerField(blank=True, null=True)
    코로나_여부 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dong_data'
