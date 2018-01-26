from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.DoubtsHome.as_view(),name="doubtshome"),
    url(r'^ask-question/$',views.AskQuestionFormView.as_view(), name="AskQuestion"),
    url(r'^upvote/$',views.upvote,name="upvotes"),
    url(r'^vote/$',views.vote,name="votes"),
    url(r'^(?P<slug>[\w-]+)/$',views.QuestionDetail.as_view(),name="Questiondetail"),
]