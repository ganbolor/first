from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.hrms.position.views',
    url(r'^$', 'index', name='index'),
    
)
