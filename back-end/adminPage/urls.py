from django.urls import path
from . import views

urlpatterns = [
    path('userlist/<str:function>/<str:first>/<str:second>', views.UserList.as_view()),
    path('usermanage/<int:user_id>', views.UserManager.as_view()),
    path('commentmanage/<int:category>/<int:comment_id>', views.ManageComment.as_view()),
    path('manageboard/<str:category>/<int:post_id>', views.ManageBoard.as_view()),
    # path('suggestions/updatepost/<int:pk>', views.SuggestionUpdateView.as_view()),
    # path('suggestions/deletepost/<int:pk>', views.SuggestionDeleteView.as_view())
]