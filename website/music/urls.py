#url configuration for music
from django.conf.urls import url
from . import views

app_name='music'
urlpatterns=[

	#url(r'^$',views.index,name='index'),
	#url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
	#/music/id/favourite
	#url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
	#/music/
	url(r'^$',views.IndexView.as_view(),name='index'),
	#/music/id/
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
	#/music/album/add/
	url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),
]
