from django.conf.urls import patterns, url

urlpatterns = patterns('apps.hrms.interactive.views',
    url(r'^$', 'index', name='index'),
    
    url(r'^intCustomersList/', 'intCustomersList'),
    
    
)
