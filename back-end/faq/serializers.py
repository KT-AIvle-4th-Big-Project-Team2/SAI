from rest_framework import serializers
from .models import Faq

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'faq_id',
            'title',
            'contents',
            'creationdate',
            'admin_admin',
        )
        model = Faq


