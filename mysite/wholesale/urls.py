from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loginpage, name='loginpage'),
    url(r'^invalidlogin/$', views.invalidlogin, name='invalidlogin'),
    url(r'^loginauth/$', views.loginauth, name='loginauth'),
    url(r'^logoutauth/$', views.logoutauth, name='logoutauth'),
    url(r'^customer/(?P<cid>[0-9]+)/$', views.customerpage, name='customerpage'),
    url(r'^customer/(?P<cid>[0-9]+)/order/$', views.customerorder, name='customerorder'),
    url(r'^customer/(?P<cid>[0-9]+)/placeorder/$', views.placeorder, name="placeorder"),
]