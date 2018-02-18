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
    url(r'^$',views.TestList.as_view(), name="testlist"),
    url(r'^add_test_paper/$',views.AddTestView.as_view(), name="add_test_paper"),
    url(r'^add_test_paper/add_question/(?P<slug>[\w-]+)/$',views.AddQuestionView.as_view(), name="add_question"),
    url(r'^add_test_paper/marksheet/(?P<slug>[\w-]+)/$',views.Marksheet.as_view(), name="marksheet"),
    url(r'^(?P<slug>[\w-]+)/$',views.TestPaperView.as_view(), name="testpaper"),

]
