from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='details'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote),
]