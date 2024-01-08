from .models import *
from rest_framework import serializers


class DongReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dong_report_data
        fields = '__all__'

class MarketReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market_report_data
        fields = '__all__'
        
        
class seoul_rent_Serializer(serializers.ModelSerializer):
    class Meta:
        model = seoul_rent_db
        fields = '__all__'
        
        
class vacancyrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = vacancyrate_db
        fields = '__all__'


class franchise_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = franchise_data
        fields = '__all__'
        
        
