from django.conf.urls import url
from django.contrib import admin
from faces import views

urlpatterns = [
	url(r'^appcall', views.appcall, name='appcall'),
    url(r'^submit', views.homepage.as_view(), name='submit'),
	url(r'^score', views.homepage.as_view(), name='home'),
    url(r'^$', views.master.as_view(), name='master'),
]