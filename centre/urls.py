"""centre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.views.generic import TemplateView
from tests.views import AboutView
from blog.views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [

    
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^blog/', include('blog.urls',namespace="blog")),
    url(r'^doubts/',include('doubts.urls',namespace="doubts")),
    url(r'^tests/',include('tests.urls',namespace="tests")),
    url(r'^users/',include('Users.urls',namespace="users")),
    url(r'^about/$',AboutView.as_view(),name="about"),
    url(r'^notes/', include("notes.urls", namespace="notes")),
    url(r'^study/material/', include("study_material.urls", namespace="study_material")),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
