# Generated by Django 4.2 on 2024-01-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis", "0002_dongservicedataestimatetestfullfin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AiReport",
            fields=[
                ("report_id", models.AutoField(primary_key=True, serialize=False)),
                ("creationdate", models.DateTimeField(auto_now_add=True)),
                ("region", models.CharField(max_length=20)),
                ("area", models.CharField(max_length=20)),
                ("business", models.CharField(max_length=20)),
                ("funds", models.BigIntegerField()),
                ("sales_23_2q", models.BigIntegerField(blank=True, null=True)),
                ("esti_23_3q", models.BigIntegerField(blank=True, null=True)),
                ("pred_23_4q", models.BigIntegerField(blank=True, null=True)),
                ("top_influ", models.JSONField(blank=True, null=True)),
                ("bottom_influ", models.JSONField(blank=True, null=True)),
                ("sim_result", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "avg_sale_comp",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("sale_updown", models.CharField(blank=True, max_length=45, null=True)),
                (
                    "market_active",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                (
                    "opening_updown",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("area_growth", models.CharField(blank=True, max_length=45, null=True)),
                (
                    "fpeople_updown",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                (
                    "simil_area_name_1",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("simil_area_esti_1", models.BigIntegerField(blank=True, null=True)),
                ("simil_area_diff_1", models.BigIntegerField(blank=True, null=True)),
                (
                    "simil_area_name_2",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("simil_area_esti_2", models.BigIntegerField(blank=True, null=True)),
                ("simil_area_diff_2", models.BigIntegerField(blank=True, null=True)),
                ("AI", models.CharField(db_column="AI", max_length=10)),
            ],
            options={
                "db_table": "ai_report",
                "managed": False,
            },
        ),
    ]