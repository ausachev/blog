#coding=utf-8
from settings import MEDIA_ROOT
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',include('mysite.weblog.urls')),
    # url(r'^search',views.search),
    url(r'^blog/',include('mysite.weblog.urls')),
    # url(r'^blog/',views.blog_page), #
    url(r'^medias/(?P<path>.*)', 'mysite.dynamic_media_serve.serve', 
                                                {'document_root': MEDIA_ROOT,
                                                    }),
    )