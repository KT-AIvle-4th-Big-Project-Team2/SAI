"""
URL configuration for dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

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
    
    #
    path('report/', include("report.urls")),
    path('fileupload/', include("fileupload.urls")),
    path("gallery/", include ('gallery.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)