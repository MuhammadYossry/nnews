from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.news, name="index"),
	url(r'^news/$', views.news_list, name='news_list'),
    # url(r'^news/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
]