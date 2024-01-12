
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("accounts/", include("account.urls")),
    path('board/', include('board.urls')),
    path('consultboard/', include('consultBoard.urls')),
    path('announcement/', include('announcement.urls')),
    path('suggestions/', include('suggestions.urls')),
    path('faq/', include("faq.urls")),
    path('analysis/', include("analysis.urls")),
    path('adminpage/', include("adminPage.urls")),
    path('userPage/', include("userPage.urls")),
    path('report/', include("report.urls")),
    path('file/',include("fileupload.urls"))
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)