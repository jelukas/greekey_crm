from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jobcontrol.views.index', name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^jobcontrol/', include('jobcontrol.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,show_indexes=False)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)