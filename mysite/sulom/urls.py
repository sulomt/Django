#url configuration for sulom
from django.conf.urls import url,include
from . import views

urlpatterns = [
	 url(r'^$', views.index_s,name='index_s'),
	 url(r'^contact/$', views.contact, name='contact'),
]
