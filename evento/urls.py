from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.list_evento, name = "listEvento"),
	url(r'^add$', views.register_evento, name = "addEvento"),
	url(r'^update/(?P<id>.+)/$', views.update_evento, name = "updateEvento"),
	url(r'^delete/(?P<id>.+)/$', views.delete_evento, name = "deleteEvento"),
	url(r'^details/(?P<id>.+)/$', views.details_evento, name = "detailsEvento"),
]