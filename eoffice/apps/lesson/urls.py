from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.lesson.views',
    url(r'^$', 'index', name='index'),
    
    
)
