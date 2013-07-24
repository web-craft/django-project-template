from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^{0}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
