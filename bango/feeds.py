# -*- coding: utf-8 -*-
from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from Bango.blog.models import Post
from Bango.blog.views import BANGO_VERSION

class LatestPosts(Feed):
    title = "::afronski blog ["+ BANGO_VERSION + "]::"
    link = "/blog/"
    description = title + " :: ostatnie posty"
    author_email = "afronski@gmail.com"
    author_name = "afronski"
    feed_type = Atom1Feed
    
    def item_pubdate(self, item):
	return item.date_created

    def items(self):
        return Post.objects.order_by('-date_created')[:10]

    def __unicode__(self):
        return unicode(self.title)
