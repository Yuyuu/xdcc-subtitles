from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^start$', views.start, name='start'),
    url(r'^stop$', views.stop, name='stop'),
    url(r'^health$', views.health_check, name='health_check')
]