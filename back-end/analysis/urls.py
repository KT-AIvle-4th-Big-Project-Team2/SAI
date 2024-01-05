from django.urls import path
from . import views

urlpatterns = [
    
    path("signin/", views.dong_predict.as_view()),
    path("checkauth/", views.dong_estimate.as_view()),
    path("checkauth/", views.market_predict.as_view()),
    path("checkauth/", views.market_estimate.as_view()),
    
]