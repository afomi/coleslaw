from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    (r'^laws/', include('laws.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {'template': 'index.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
