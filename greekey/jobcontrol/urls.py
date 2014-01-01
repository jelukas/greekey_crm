from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^start/$', 'jobcontrol.views.start_general_timer', name='start_general_timer'),
	url(r'^stop/$', 'jobcontrol.views.stop_general_timer', name='stop_general_timer'),
)