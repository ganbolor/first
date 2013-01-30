from django.conf.urls import patterns, url

urlpatterns = patterns('apps.setting.views',
    url(r'^$', 'index', name='index'),
    
    url(r'^appmodule/$',        'appmoduleIndex'),
    url(r'^appmodule/list/$',   'appmoduleList'),
    url(r'^appmodule/add/$',    'appmoduleAdd'),
    url(r'^appmodule/view/(?P<object_id>\d+)/$',    'appmoduleView'),
    url(r'^appmodule/del/(?P<object_id>\d+)/$',     'appmoduleDel'),
    url(r'^appmodule/edit/(?P<object_id>\d+)/$',    'appmoduleEdit'),
    
    url(r'^config/$',           'configIndex'),
    url(r'^config/list/$',      'configList'),
    url(r'^config/add/$',       'configAdd'),
    url(r'^config/view/(?P<object_id>\d+)/$',   'configView'),
    url(r'^config/del/(?P<object_id>\d+)/$',    'configDel'),
    url(r'^config/edit/(?P<object_id>\d+)/$',   'configEdit'),
)
