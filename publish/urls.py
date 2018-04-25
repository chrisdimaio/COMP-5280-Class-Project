from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.publish_word, name='publish_word'),
    # url(r'^post/(?P<pk>\d+)/$', views.publish_detail, name='publish_detail'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^publish/new/$', views.PublishView.as_view(), name='publish'),
    # url(r'^words/$', views.WordsView.as_view(), name='words'),
]