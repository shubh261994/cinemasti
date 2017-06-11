from django.conf.urls import url
from django.contrib import admin
from .views import (
	movies_list,
	movies_detail,
	in_theaters,
	coming_soon,
	movies_genre
	)

urlpatterns = [
    url(r'^$', movies_list, name = 'list'),
    url(r'^in_theaters/$', in_theaters, name = 'in_theaters'),
    url(r'^coming_soon/$', coming_soon, name = 'coming_soon'),
    url(r'^genre/(?P<genre>[\w-]+)$', movies_genre, name = "movies_genre"),
    url(r'^(?P<slug>[\w-]+)$', movies_detail, name = "detail"),
]