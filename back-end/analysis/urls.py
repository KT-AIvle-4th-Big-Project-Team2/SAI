from django.urls import path
from . import views

urlpatterns = [
    
    path("dongai/<str:goo>/<str:dong>/<str:business>/<int:funds>", views.dong_ai.as_view()),
    #path("dongpredict/<str:goo>/<str:dong>/<str:business>/<int:funds>", views.dong_predict.as_view()),
    
    path("marketestimate/<str:goo>/<str:market>/<str:business>/<int:funds>", views.market_ai.as_view()),
    # path("marketpredict/<str:market>/<str:business>/<int:funds>", views.market_predict.as_view()),
    
    
]