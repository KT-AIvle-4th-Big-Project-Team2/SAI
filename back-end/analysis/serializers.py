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