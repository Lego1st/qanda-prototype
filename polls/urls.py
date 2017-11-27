from django.conf.urls import url 

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='details'),
	url(r'^new_question/$', views.new_question, name='newquestion'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote),
]