from django.urls import path
from . import views

urlpatterns = [
    path("dongreport/<str:dong>/<str:business>", views.dong_report.as_view()),
    path("marketreport/<str:market>/<str:business>", views.market_report.as_view()),
    
    ]