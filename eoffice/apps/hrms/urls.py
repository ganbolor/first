from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.hrms.views',
    url(r'^$', 'index', name='index'),
    
    #url(r'^department/', include('apps.hrms.interactive.urls')),
    ##url(r'^position/', include('apps.hrms.interactive.urls')),
    #url(r'^employee/', include('apps.hrms.interactive.urls')),
    
    url(r'^interactive/', include('apps.hrms.interactive.urls')),
    url(r'^department/', include('apps.hrms.department.urls')),
    url(r'^position/', include('apps.hrms.position.urls')),
    url(r'^employee/', include('apps.hrms.employee.urls')),
    
    
)
