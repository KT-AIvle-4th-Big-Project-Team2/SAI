from django.urls import path
from . import views

urlpatterns = [
   
    path("signin/", views.SignInView.as_view()), #
    path("login/", views.LoginView.as_view()), #
    path('logout/', views.LogoutView.as_view()), #
    path("getuser/<str:username>", views.GetUserView.as_view()), #
    path("deleteuser/<str:username>", views.DeleteAccountView.as_view()),
    path("checkpassword/", views.CheckPWView.as_view()), #
    path("updateuser/<str:username>", views.UpdateUserInfo.as_view()),
    path("findpw/", views.findPWView.as_view()),
    # path("updatepw/", views.UpdatePWView.as_view()), #
    # path("findid/", views.FindIDView.as_view()),#
    # path("resetpw/", views.ResetPW.as_view()), #
    # path("checkauth/", views.CheckAuthenticatedView.as_view()), #
    # path("getcsrf/", views.GetCSRFToken.as_view()), #
]
