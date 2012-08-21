from django.conf.urls import patterns, include, url

urlpatterns = patterns('fileserver.views',
    url(r'^$', 'frontpage', name='fileserver_frontpage'),
    url(r'^login$', 'login', name='fileserver_login'),
    url(r'^logout$', 'logout', name='fileserver_logout'),
    url(r'^index/(?P<path>.*)', 'serve_directory', name='fileserver_directory'),
    url(r'^download/(?P<path>.*)', 'download', name='fileserver_download'),
    url(r'^upload/(?P<path>.*)', 'upload', name='fileserver_upload'),
)
