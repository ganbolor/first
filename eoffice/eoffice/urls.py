from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eoffice.views.home', name='home'),
    # url(r'^eoffice/', include('eoffice.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout' ),
    #url(r'^accounts/password_change/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout' ),
    #url(r'^accounts/profile/$', include('apps.home.urls')),
    
    
    url(r'^accounts/', include('apps.auth.urls')),
    
    
    url(r'^$',        include('apps.home.urls'), name='home'),
    
    url(r'^hrms/',    include('apps.hrms.urls')),
    
    url(r'^setting/', include('apps.setting.urls')),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    
) 

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
else:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)