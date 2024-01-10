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
    area = models.CharField(max_length=20)
    number_23_2q_sales = models.BigIntegerField(db_column='23_2q_sales', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_23_4q_esti = models.BigIntegerField(db_column='23_4q_esti', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_23_3q_sales = models.BigIntegerField(db_column='23_3q_sales', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_23_4q_pre = models.BigIntegerField(db_column='23_4q_pre', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    top_influ = models.JSONField(blank=True, null=True)
    bottom_influ = models.JSONField(blank=True, null=True)
    sim_result = models.CharField(max_length=10, blank=True, null=True)
    avg_sale_comp = models.CharField(max_length=45, blank=True, null=True)
    sale_updown = models.CharField(max_length=45, blank=True, null=True)
    market_active = models.CharField(max_length=45, blank=True, null=True)
    opening_updown = models.CharField(max_length=45, blank=True, null=True)
    area_growth = models.CharField(max_length=45, blank=True, null=True)
    fpeople_updown = models.CharField(max_length=45, blank=True, null=True)
    simil_area_name_1 = models.CharField(max_length=20, blank=True, null=True)
    simil_area_esti_1 = models.BigIntegerField(blank=True, null=True)
    simil_area_diff_1 = models.BigIntegerField(blank=True, null=True)
    simil_area_name_2_field = models.CharField(db_column='simil_area_name_2:', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    simil_area_esti_2 = models.BigIntegerField(blank=True, null=True)
    simil_area_diff_2 = models.BigIntegerField(blank=True, null=True)
    ai = models.CharField(db_column='AI', max_length=10)  # Field name made lowercase.
    user = models.ForeignKey('AccountUsercustom', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ai_report'
