"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from apps.image.views import ImageViewSet
from apps.user.views import UserViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UserViewSet)
router_v1.register(r'images', ImageViewSet)

api_v1 = [
    url(r'auth/obtain/', obtain_jwt_token)
] + router_v1.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(api_v1))
]

# This is an inefficient helper for viewing images during development.
# It does NOT work when `DEBUG = False`.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
