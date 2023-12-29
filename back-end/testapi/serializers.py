from rest_framework import serializers

        

class test_data(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.TimeField()

