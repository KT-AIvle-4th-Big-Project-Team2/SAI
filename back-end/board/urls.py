from django.urls import path
from . import views


urlpatterns = [
    # path('', views.ListPost.as_view()),
    # path('<int:pk>', views.DetailPost.as_view()),
    path('postlist/', views.CustomSerializer1.as_view()),
    path('postlist/<int:pk>', views.CustomSerializer2.as_view()),
    path('postlist/createpost', views.CustomSerializer3.as_view())
]