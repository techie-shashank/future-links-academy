from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/$', views.TopicDetailView.as_view(), name="topic_detail"),
    url(r'^list/(?P<pk>\d+)/$', views.ChapterListView.as_view(), name="chapter_list"),
    url(r'^notes-home/$', views.NotesPageView.as_view(), name="notes_home"),
]
