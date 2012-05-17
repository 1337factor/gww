from django.conf.urls import patterns, url


urlpatterns = patterns('www.views',
	url(r'^$', 'index', name='www.index'),

    #Test test page :)
	url(r'^test$', 'test', name='www.test'),
)
  