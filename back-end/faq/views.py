
from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Faq
from .serializers import *

class ListPost(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer