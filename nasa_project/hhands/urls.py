from django.conf.urls import url
from django.urls import include, path                                                                                                                              
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("app/", views.app, name='app'),
    path("about/", views.about, name='about'),
]