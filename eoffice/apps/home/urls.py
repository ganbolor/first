from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.home.views',
    url(r'^$', 'index', name='index'),
    url(r'^home/', 'index'),
    #url(r'^mypage/', 'dashboard'),
)
