from .models import *
from rest_framework import serializers


class DongServiceEstimateFinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DongServiceDataEstimateTestFullFin
        fields = '__all__'
        
        
class DongServiceEstimateShapValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DongServiceEstimateShapValues
        fields = '__all__'
        
        
        
        
class MarketSortedDbFinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketSortedDbFin
        fields = ['점포별_평균_매출_금액']
        
class MarketServiceEstimateShapValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketServiceEstimateShapValues
        fields = '__all__'
        
        
class AIReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AiReport
        fields = '__all__'

class AIReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiReport
        fields = ['creationdate', 'region', 'area', 'business', 'funds', 'sim_result', 'report_id']
        
        
