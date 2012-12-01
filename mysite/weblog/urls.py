from django.conf.urls.defaults import *
# from weblog.views import *
from mysite.weblog import views
urlpatterns = patterns('',

          url(r'^$',views.base,name='base'),
          url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',views.archive,name ='archive'),

)