from rest_framework import serializers
from .models import Board
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'board_id',
            'title',
            'contents',
            'tag',
            'creationdate',
            'user',
        )
        model = Board