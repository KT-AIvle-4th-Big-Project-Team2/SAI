from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.testing),
    path("signin/", views.signIn),
    path("signin/new_account_success/", views.signinSuccess),
    path("login/", views.login)
]
