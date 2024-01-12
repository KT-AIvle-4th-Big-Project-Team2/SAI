from . import views
from django.urls import path

app_name = 'report'

urlpatterns = [
    path("dongreport/<str:dong>/<str:business>", views.dong_report.as_view()),
    path("marketreport/<str:market>/<str:business>", views.market_report.as_view()),
    
    
    #path("dongreport/", views.rent_cost.as_view()),
    
    
    #path("dongreport/", views.dong_report.as_view()),
    # path("dongreport/", views.franchisedata.as_view()),
    
    ]