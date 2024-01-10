# from . import views
# from django.urls import path

# app_name = 'report'

<<<<<<< HEAD
# urlpatterns = [
#     path("", views.inquire),
#     path("recommendation/<business>/<seedMoney>", views.recommendation, name = "recommendation"),
# ]
=======
urlpatterns = [
    #path("dongreport/<str:goo>/<str:dong>/<str:business>/<int:seedMoney>", views.dong_ai.as_view()),
    #path("dongreport/<str:goo>/<str:dong>", views.franchise_report.as_view()),
    
    
    #path("dongreport/", views.rent_cost.as_view()),
    
    
    path("dongreport/", views.dong_report.as_view()),
    path("marketreport/", views.market_report.as_view()),
    #path("dongreport/", views.franchisedata.as_view()),
    
    ]
>>>>>>> 8c2c4221f2d47476228d758eba29746d3c7d0e1f
