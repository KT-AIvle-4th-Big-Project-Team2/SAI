from django.urls import path
from . import views

urlpatterns = [
    path("dongai/<str:username>/<str:goo>/<str:business>/<int:funds>/<str:dong>", views.dong_ai.as_view()),
    path("marketai/<str:username>/<str:goo>/<str:business>/<int:funds>/<str:market>", views.market_ai.as_view()),
        
    
    
    path("reportlist/<str:username>", views.AIReportListView.as_view()),
    path("reportlist/<str:username>/<int:num>", views.AIReportView.as_view()),
    path("reportlist/<str:username>/<int:num>/delete", views.AIReportDeleteView.as_view()),
    # path("rentcost", views.rent_cost.as_view()),
    # path("franchise", views.franchisedata.as_view()),
    #path("rentcost", views.rent_cost.as_view())
]