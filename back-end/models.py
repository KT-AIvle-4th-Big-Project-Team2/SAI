# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AiReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    creationdate = models.DateTimeField()
    region = models.CharField(max_length=20)
    area_1 = models.CharField(max_length=20)
    area_2 = models.CharField(max_length=20, blank=True, null=True)
    business = models.CharField(max_length=20)
    funds = models.BigIntegerField()
    ai = models.CharField(db_column='AI', max_length=10)  # Field name made lowercase.
    sales_23_2q = models.BigIntegerField(blank=True, null=True)
    esti_23_3q = models.BigIntegerField(blank=True, null=True)
    pred_23_4q = models.BigIntegerField(blank=True, null=True)
    top_influ = models.JSONField(blank=True, null=True)
    bottom_influ = models.JSONField(blank=True, null=True)
    sim_result = models.CharField(max_length=10, blank=True, null=True)
    avg_sale_comp = models.IntegerField(blank=True, null=True)
    sale_updown = models.CharField(max_length=20, blank=True, null=True)
    market_active = models.CharField(max_length=20, blank=True, null=True)
    opening_updown = models.CharField(max_length=20, blank=True, null=True)
    area_growth = models.CharField(max_length=20, blank=True, null=True)
    fpeople_updown = models.CharField(max_length=20, blank=True, null=True)
    simil_area_name_1 = models.CharField(max_length=20, blank=True, null=True)
    simil_area_esti_1 = models.BigIntegerField(blank=True, null=True)
    simil_area_diff_1 = models.BigIntegerField(blank=True, null=True)
    simil_area_name_2 = models.CharField(max_length=20, blank=True, null=True)
    simil_area_esti_2 = models.BigIntegerField(blank=True, null=True)
    simil_area_diff_2 = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('AccountUsercustom', models.DO_NOTHING)
    rent_cost = models.IntegerField(blank=True, null=True)
    posi_fran_num = models.IntegerField(blank=True, null=True)
    franchise_rec_1 = models.JSONField(blank=True, null=True)
    franchise_rec_2 = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_report'
