from django.contrib import admin
from django.conf.urls import url, include
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
    # /login
    url(r'', include('django.contrib.auth.urls')),
    # /signup
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
    # /admin - manage accounts
    url(r'^admin/', admin.site.urls),
    # /up_vote
    url(r'^up_vote/$', views.up_vote, name='up_vote'),
    # /down_vote
    url(r'^down_vote/$', views.down_vote, name='down_vote'),
    # /user_def
    url(r'^user_def/(?P<word_value>[a-z]+)$', views.user_def, name='user_def')
]
