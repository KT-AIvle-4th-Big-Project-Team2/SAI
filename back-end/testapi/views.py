from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status









class CustomDataAPIView(APIView):
    def get(self, request):
        # 여기에서 원하는 데이터를 전처리하여 가져온다.
        custom_data = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
            # 추가적인 데이터를 필요에 따라 포함
        ]

        # 데이터를 JSON으로 응답
        return Response(custom_data, status=status.HTTP_200_OK)

    

    