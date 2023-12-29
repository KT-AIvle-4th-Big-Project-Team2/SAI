from django.urls import path

from testapi.views import CustomDataAPIView

urlpatterns = [
     path('customdata/', CustomDataAPIView.as_view(), name='customdata-api'),
]