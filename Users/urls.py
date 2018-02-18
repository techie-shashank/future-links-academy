from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,logout


urlpatterns = [
	url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',logout, {'next_page': '/'},name="logout"),
    url(r'^register/',views.RegisterView,name="register"),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]