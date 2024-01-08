# Generated by Django 5.0.1 on 2024-01-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DongSortedDbFin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("기준_년분기_코드", models.IntegerField(blank=True, null=True)),
                ("행정동_코드", models.IntegerField(blank=True, null=True)),
                ("행정동_코드_명", models.TextField(blank=True, null=True)),
                ("서비스_업종_코드", models.TextField(blank=True, null=True)),
                ("서비스_업종_코드_명", models.TextField(blank=True, null=True)),
                ("당월_매출_금액", models.FloatField(blank=True, null=True)),
                ("당월_매출_건수", models.IntegerField(blank=True, null=True)),
                ("주중_매출_금액", models.FloatField(blank=True, null=True)),
                ("주말_매출_금액", models.FloatField(blank=True, null=True)),
                ("월요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("화요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("수요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("목요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("금요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("토요일_매출_금액", models.FloatField(blank=True, null=True)),
                ("일요일_매출_금액", models.FloatField(blank=True, null=True)),
                (
                    "시간대_00_06_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_00~06_매출_금액", null=True
                    ),
                ),
                (
                    "시간대_06_11_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_06~11_매출_금액", null=True
                    ),
                ),
                (
                    "시간대_11_14_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_11~14_매출_금액", null=True
                    ),
                ),
                (
                    "시간대_14_17_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_14~17_매출_금액", null=True
                    ),
                ),
                (
                    "시간대_17_21_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_17~21_매출_금액", null=True
                    ),
                ),
                (
                    "시간대_21_24_매출_금액",
                    models.FloatField(
                        blank=True, db_column="시간대_21~24_매출_금액", null=True
                    ),
                ),
                ("남성_매출_금액", models.FloatField(blank=True, null=True)),
                ("여성_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_10_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_20_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_30_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_40_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_50_매출_금액", models.FloatField(blank=True, null=True)),
                ("연령대_60_이상_매출_금액", models.FloatField(blank=True, null=True)),
                ("주중_매출_건수", models.IntegerField(blank=True, null=True)),
                ("주말_매출_건수", models.IntegerField(blank=True, null=True)),
                ("월요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("화요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("수요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("목요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("금요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("토요일_매출_건수", models.IntegerField(blank=True, null=True)),
                ("일요일_매출_건수", models.IntegerField(blank=True, null=True)),
                (
                    "시간대_건수_06_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~06_매출_건수", null=True
                    ),
                ),
                (
                    "시간대_건수_11_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~11_매출_건수", null=True
                    ),
                ),
                (
                    "시간대_건수_14_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~14_매출_건수", null=True
                    ),
                ),
                (
                    "시간대_건수_17_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~17_매출_건수", null=True
                    ),
                ),
                (
                    "시간대_건수_21_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~21_매출_건수", null=True
                    ),
                ),
                (
                    "시간대_건수_24_매출_건수",
                    models.IntegerField(
                        blank=True, db_column="시간대_건수~24_매출_건수", null=True
                    ),
                ),
                ("남성_매출_건수", models.IntegerField(blank=True, null=True)),
                ("여성_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_10_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_20_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_30_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_40_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_50_매출_건수", models.IntegerField(blank=True, null=True)),
                ("연령대_60_이상_매출_건수", models.IntegerField(blank=True, null=True)),
                ("집객시설_수", models.FloatField(blank=True, null=True)),
                ("관공서_수", models.FloatField(blank=True, null=True)),
                ("은행_수", models.FloatField(blank=True, null=True)),
                ("종합병원_수", models.FloatField(blank=True, null=True)),
                ("일반_병원_수", models.FloatField(blank=True, null=True)),
                ("약국_수", models.FloatField(blank=True, null=True)),
                ("유치원_수", models.FloatField(blank=True, null=True)),
                ("초등학교_수", models.FloatField(blank=True, null=True)),
                ("중학교_수", models.FloatField(blank=True, null=True)),
                ("고등학교_수", models.FloatField(blank=True, null=True)),
                ("대학교_수", models.FloatField(blank=True, null=True)),
                ("백화점_수", models.FloatField(blank=True, null=True)),
                ("슈퍼마켓_수", models.FloatField(blank=True, null=True)),
                ("극장_수", models.FloatField(blank=True, null=True)),
                ("숙박_시설_수", models.FloatField(blank=True, null=True)),
                ("공항_수", models.FloatField(blank=True, null=True)),
                ("철도_역_수", models.FloatField(blank=True, null=True)),
                ("버스_터미널_수", models.FloatField(blank=True, null=True)),
                ("지하철_역_수", models.FloatField(blank=True, null=True)),
                ("버스_정거장_수", models.FloatField(blank=True, null=True)),
                ("총_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_10_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_20_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_30_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_40_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_50_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_60_이상_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_10_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_20_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_30_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_40_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_50_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_60_이상_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_10_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_20_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_30_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_40_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_50_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_60_이상_직장_인구_수", models.IntegerField(blank=True, null=True)),
                ("점포_수", models.IntegerField(blank=True, null=True)),
                ("유사_업종_점포_수", models.IntegerField(blank=True, null=True)),
                ("개업_율", models.IntegerField(blank=True, null=True)),
                ("개업_점포_수", models.IntegerField(blank=True, null=True)),
                ("폐업_률", models.IntegerField(blank=True, null=True)),
                ("폐업_점포_수", models.IntegerField(blank=True, null=True)),
                ("프랜차이즈_점포_수", models.IntegerField(blank=True, null=True)),
                ("아파트_단지_수", models.IntegerField(blank=True, null=True)),
                ("아파트_면적_66_제곱미터_미만_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_면적_66_제곱미터_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_면적_99_제곱미터_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_면적_132_제곱미터_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_면적_165_제곱미터_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_1_억_미만_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_1_억_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_2_억_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_3_억_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_4_억_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_5_억_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_가격_6_억_이상_세대_수", models.FloatField(blank=True, null=True)),
                ("아파트_평균_면적", models.IntegerField(blank=True, null=True)),
                ("아파트_평균_시가", models.FloatField(blank=True, null=True)),
                ("월_평균_소득_금액", models.IntegerField(blank=True, null=True)),
                ("소득_구간_코드", models.IntegerField(blank=True, null=True)),
                ("지출_총금액", models.FloatField(blank=True, null=True)),
                ("식료품_지출_총금액", models.FloatField(blank=True, null=True)),
                ("의류_신발_지출_총금액", models.FloatField(blank=True, null=True)),
                ("생활용품_지출_총금액", models.FloatField(blank=True, null=True)),
                ("의료비_지출_총금액", models.FloatField(blank=True, null=True)),
                ("교통_지출_총금액", models.FloatField(blank=True, null=True)),
                ("교육_지출_총금액", models.FloatField(blank=True, null=True)),
                ("유흥_지출_총금액", models.FloatField(blank=True, null=True)),
                ("여가_문화_지출_총금액", models.FloatField(blank=True, null=True)),
                ("기타_지출_총금액", models.FloatField(blank=True, null=True)),
                ("음식_지출_총금액", models.FloatField(blank=True, null=True)),
                ("총_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_10_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_20_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_30_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_40_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_50_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_60_이상_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_10_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_20_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_30_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_40_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_50_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성연령대_60_이상_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_10_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_20_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_30_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_40_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_50_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성연령대_60_이상_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("총_가구_수", models.IntegerField(blank=True, null=True)),
                ("아파트_가구_수", models.IntegerField(blank=True, null=True)),
                ("비_아파트_가구_수", models.IntegerField(blank=True, null=True)),
                ("총_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("남성_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("여성_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_10_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_20_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_30_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_40_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_50_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_60_이상_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_00_06_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_06_11_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_11_14_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_14_17_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_17_21_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_21_24_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("월요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("화요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("수요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("목요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("금요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("토요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("일요일_유동인구_수", models.IntegerField(blank=True, null=True)),
                ("점포별_평균_매출_금액", models.FloatField(blank=True, null=True)),
                ("분기", models.IntegerField(blank=True, null=True)),
                ("코로나_여부", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "dong_sorted_db_fin",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="FranchiseData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("대분류서비스", models.TextField(blank=True, null=True)),
                ("중분류서비스", models.TextField(blank=True, null=True)),
                ("법인명", models.TextField(blank=True, null=True)),
                ("브랜드명", models.TextField(blank=True, null=True)),
                ("가맹점수", models.IntegerField(blank=True, null=True)),
                (
                    "신규가맹점_등록수",
                    models.IntegerField(blank=True, db_column="신규가맹점 등록수", null=True),
                ),
                ("계약종료수", models.IntegerField(blank=True, null=True)),
                ("계약해지수", models.IntegerField(blank=True, null=True)),
                ("명의변경수", models.IntegerField(blank=True, null=True)),
                ("평균매출금액", models.IntegerField(blank=True, null=True)),
                ("면적단위평균매출액", models.IntegerField(blank=True, null=True)),
                ("가맹금액", models.IntegerField(blank=True, null=True)),
                ("교육금액", models.IntegerField(blank=True, null=True)),
                ("보증금액", models.IntegerField(blank=True, null=True)),
                ("기타금액", models.IntegerField(blank=True, null=True)),
                ("합계금액", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "franchise_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Vacancyrate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("지역별", models.TextField(blank=True, null=True)),
                ("상세지역", models.TextField(blank=True, null=True)),
                ("임대료", models.FloatField(blank=True, null=True)),
                ("평균임대면적", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "vacancyrate",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Report",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
