from django.conf.urls import url, include
from main import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^loginpage$', views.loginpage),
   url(r'^doLogin$', views.doLogin),
   url(r'^doLogout$', views.doLogout),
   url(r'^partials/([a-zA-Z]+).html$', views.servePartial),
   url(r'', include('django.contrib.auth.urls', namespace='auth')),
   url(r'', include('social.apps.django_app.urls', namespace='social')),
]
