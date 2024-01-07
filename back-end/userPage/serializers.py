from rest_framework import serializers

from account.models import *
from board.models import *
from consultBoard.models import *
from suggestions.models import *
from .models import *

class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"