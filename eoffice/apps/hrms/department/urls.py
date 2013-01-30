from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.hrms.deparment.views',
    url(r'^$', 'index', name='index'),
    
)
