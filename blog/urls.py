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
from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$',views.BlogHome.as_view(),name="bloghome"),
    url(r'^create/$',views.AddPostCreateFormView.as_view(), name="addposts"),
    url(r'^like/$',views.like,name="likes"),
    url(r'^category_list/(?P<category>[\w-]+)/$',views.category_list_view,name="category_list"),
    url(r'^update/(?P<slug>[\w-]+)/$',views.PostUpdate.as_view(),name="postupdate"),
    url(r'^delete/(?P<slug>[\w-]+)/$',views.PostDelete.as_view(),name="postdelete"),
    url(r'^(?P<slug>[\w-]+)/$',views.PostDetail.as_view(),name="postdetail"),
]
