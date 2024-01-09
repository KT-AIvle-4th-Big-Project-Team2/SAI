from . import views
from django.urls import path

app_name = 'report'

urlpatterns = [
    #path("dongreport/<str:goo>/<str:dong>/<str:business>/<int:seedMoney>", views.dong_ai.as_view()),
    #path("dongreport/<str:goo>/<str:dong>", views.franchise_report.as_view()),
    
    
    #path("dongreport/", views.rent_cost.as_view()),
    
    
    path("dongreport/", views.dong_report.as_view()),
    #path("dongreport/", views.franchisedata.as_view()),
    #path("dongreport/", views.franchisedata.as_view()),
    
    ]