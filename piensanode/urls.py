from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *
from maploom.geonode.urls import urlpatterns as maploom_urls
from hypermap.urls import urlpatterns as registry_urls

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
 ) + urlpatterns

urlpatterns += maploom_urls
urlpatterns += registry_urls

urlpatterns = patterns('',
    url(r'^registry/client/$', 'maploom_registry.views.lennin', name='maploom_registry'),
) + urlpatterns
