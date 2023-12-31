"""HealthyRoutes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import login, register, logout, profile
from routes.views import index, saved_routes, api_route
from air_stations.views import upload_air_stations, get_provinces, get_towns, api_get_air_stations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('register/',register),
    path('logout/', logout),
    path('profile/', profile),
    path('', index),
    path('upload-air-stations', upload_air_stations),
    path('get/provinces', get_provinces),
    path('get/towns', get_towns),
    path('api/air_stations', api_get_air_stations),
    path('api/route', api_route),
    path('saved-routes/', saved_routes)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)