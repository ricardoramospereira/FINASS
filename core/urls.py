"""
URL configuration for core project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404, handler500
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'error/404_http.html', status=404)

def custom_500(request):
    return render(request, 'error/500_http.html', status=500)

handler404 = custom_404
handler500 = custom_500


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('users.urls')),
    path("investment/", include('investments.urls')),
    path("", include('dashboard.urls')),
    path("finantial/", include('financial.urls')),
    path("extract/", include('extract.urls')),
    path("planning/", include('planning.urls')),
    path("accounts/", include('accounts.urls')),

    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
