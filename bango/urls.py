from django.conf.urls.defaults import *
from django.contrib.comments.models import FreeComment
from Bango.blog.views import *
from Bango.feeds import *

feeds = {
    'latest': LatestPosts 
}

urlpatterns = patterns(
     '',
     (r'^$', frontpage),
     (r'^blog/$', frontpage),
     (r'^blog/page/(\d{1,2})/$', frontpage),
     (r'^blog/(\d{4,4})/(\d{1,2})/([\w\-]+)/$', singlepost),
     (r'^blog/(\d{4,4})/$', yearview),
     (r'^blog/(\d{4,4})/(\d{1,2})/$', monthview),
     (r'^blog/tag/([\w\-]+)/$', tagview),

     (r'^blog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),

     (r'^comments/', include('django.contrib.comments.urls.comments')),

     (r'^admin/', include('django.contrib.admin.urls'))
)

handler404 = 'Bango.error.views.err404'
handler500 = 'Bango.error.views.err500'
