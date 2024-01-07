from account.models import *
from board.models import *
from consultBoard.models import *
from faq.models import *
from suggestions.models import *
from .models import *

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
        password = models.CharField(max_length=25)
        
        class Meta:
                model = UserCustom
                fields = ['user_id', 'username', 'name', 'password', 'email', 'phonenumber', 'age', 'gender']
    