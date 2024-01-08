# Generated by Django 5.0.1 on 2024-01-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0003_dong_report_data_franchise_data_seoul_rent_db_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Market_report_data",
            fields=[
                (
                    "기준_년분기_코드",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
                ("행정동_코드", models.IntegerField(blank=True, null=True)),
                ("행정동_코드_명", models.TextField(blank=True, null=True)),
                ("서비스_업종_코드", models.TextField(blank=True, null=True)),
                ("서비스_업종_코드_명", models.TextField(blank=True, null=True)),
                ("점포_수", models.IntegerField(blank=True, null=True)),
                ("개업_점포_수", models.IntegerField(blank=True, null=True)),
                ("폐업_점포_수", models.IntegerField(blank=True, null=True)),
                ("프랜차이즈_점포_수", models.IntegerField(blank=True, null=True)),
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
                ("총_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("남성_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("여성_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_10_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_20_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_30_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_40_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_50_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("연령대_60_이상_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_00_06_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_06_11_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_11_14_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_14_17_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_17_21_상주인구_수", models.IntegerField(blank=True, null=True)),
                ("시간대_21_24_상주인구_수", models.IntegerField(blank=True, null=True)),
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
            ],
            options={
                "db_table": "market_sorted_db_fin",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="vacancyrate_db",
            fields=[
                (
                    "지역별",
                    models.TextField(blank=True, primary_key=True, serialize=False),
                ),
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
            name="Vacancyrate",
        ),
        migrations.AlterModelTable(
            name="dong_report_data",
            table="dong_sorted_db_fin",
        ),
    ]
