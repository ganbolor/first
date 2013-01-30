from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.hrms.employee.views',
    url(r'^$', 'index', name='index'),
    
    
)
