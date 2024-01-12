from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:username>', views.WrittenCommentView.as_view()),
]

