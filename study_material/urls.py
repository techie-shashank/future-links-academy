from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chapter-list/$', views.ChapterListView.as_view(), name="chapter_list"),
    url(r'^chapter/(?P<pk>\d+)/$', views.StudyMaterialView.as_view(), name="topic_detail"),
]
