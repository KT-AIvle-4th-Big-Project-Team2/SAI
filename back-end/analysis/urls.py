from django.urls import path
from . import views

urlpatterns = [
    path("dongai/<str:goo>/<str:dong>/<str:business>/<int:funds>", views.dong_ai.as_view()),
    path("marketai/<str:goo>/<str:market>/<str:business>/<int:funds>", views.market_ai.as_view()),
    path("reportlist", views.AIReportListView.as_view()),
    path("reportlist/<int:num>", views.AIReportView.as_view()),
]