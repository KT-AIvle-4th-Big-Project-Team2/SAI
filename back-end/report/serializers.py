from .models import *
from rest_framework import serializers


class DongReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DongSortedDbFin
        fields = '__all__'

class MarketReportDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MarketSortedDbFin
        fields = '__all__'
        
        
        
        
        
class seoul_rent_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SeoulRent
        fields = '__all__'
        
        
class vacancyrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancyrate
        fields = '__all__'


class franchise_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchiseData
        fields = '__all__'
        
        
