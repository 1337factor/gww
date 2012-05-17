from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
import greenww


admin.autodiscover()

urlpatterns = patterns('',
    # WEB
	(r'', include('www.urls')),

    # API
	(r'^api', include('api.urls')),

	# ADMIN
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')), url(r'^admin/', include(admin.site.urls)),

	# STATIC CONTENT
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': greenww.settings.MEDIA_ROOT}),
)
