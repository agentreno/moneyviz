from django.conf.urls import url
from main import views

urlpatterns = [
   url(r'^$', views.index),
   url(r'^login$', views.loginpage),
   url(r'^doLogin$', views.doLogin),
   url(r'^partials/([a-zA-Z]+).html$', views.servePartial),
]
