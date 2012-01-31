from django.conf.urls.defaults import *
from Vinyl.vinyl.views import playlists
from Vinyl import settings


urlpatterns = patterns('', url(r'^$', playlists),
                       (r'^Vinyl/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
                       
                       )

