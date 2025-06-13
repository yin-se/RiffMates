"""
URL configuration for RiffMates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from home import views as home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("credit/", home_views.credits, name="credits"),
    path("about_me/", home_views.about_me, name="about_me"),
    path("version_info/", home_views.version_info, name="version_info"),
    path("news/", home_views.news, name="news"),
]
