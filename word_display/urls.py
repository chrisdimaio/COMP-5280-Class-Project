from django.conf.urls import url
from . import views

urlpatterns = [
    # /word/display
    url(r'^$', views.index, name='index'),
    # /word/<word?
    url(r'^wordDef/$', views.wordDef, name='wordDef'),

    # url(r'^(?P<word_id>[a-z]+)/$', views.wordDef, name='wordDef'),
    # /word/dict_search
    url(r'^dict_search/$', views.dict_search, name='dict_search'),
    # /add_def
    url(r'^add_def/$', views.add_def, name='add_def'),
    # /about_us
    url(r'^about_us/$', views.about_us, name='about_us'),
]
