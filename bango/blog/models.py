import re
from django.db import models
from django.contrib import admin

class Post(models.Model):
    	title = models.CharField(maxlength=200)
    	slug = models.SlugField(unique=True, prepopulate_from=['title'])
    	date_created = models.DateTimeField()
    	date_modified = models.DateTimeField(auto_now=True)
    	tags = models.CharField(maxlength=200)
    	body = models.TextField()
  
    	def get_absolute_url(self):
        	return "/blog/%i/%i/%s/" % (self.date_created.year, self.date_created.month, self.slug)

    	def get_tag_list(self):
        	return re.split(" ", self.tags)

    	def __unicode__(self):
        	return unicode(self.title)
	
	def __str__(self):
        	return self.title;

	class Meta:
        	ordering = ["-date_created"]

	class Admin:
		pass
