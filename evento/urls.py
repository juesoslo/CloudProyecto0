from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.list_evento, name = "listEvento"),
	url(r'^add$', views.register_evento, name = "addEvento"),
	url(r'^update$', views.update_evento, name = "updateEvento"),
]