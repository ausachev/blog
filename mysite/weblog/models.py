#coding=utf-8
from django.db import models
from django.db.models.fields.files import ImageFieldFile
import datetime 
import sys,os
from mysite.settings import MEDIA_ROOT
from django.utils import timezone
# MEDIA_ROOT = '/uploads/image'
# Create your models here.

class BolgPost(models.Model):
	title = models.CharField(max_length= 150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	author = models.CharField(max_length= 30)
	slug = models.SlugField(help_text=("used to build the entry's URL"),
                            max_length=255) 
	images = models.ImageField(('images'), upload_to=MEDIA_ROOT,
                              blank=True ,max_length=1000,help_text=('used for illustration'))
	
	@models.permalink
	def get_absolute_url(self):
		timestamp = timezone.localtime(self.timestamp)
		# month =  str(timestamp.strftime('%b'))
		return ('archive',None,{
		'year' : timestamp.strftime('%Y'),
		'month': timestamp.strftime('%m'),
		'day'  : timestamp.strftime('%d'),
		'slug' : self.slug,
		})
	# get_absolute_url = models.permalink(get_absolute_url)

	def __unicode__(self):
		return self.title
	def get_time(self):
		timestamp = timezone.localtime(self.timestamp)
		return (self.timestamp.strftime("%Y-%b-%d"),
		)
class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	class Meta:
		verbose_name        = ('category')
		verbose_name_plural = ('categorys')
		ordering            = ('title',)
		def __unicode__(self):
			return self.title
	def get_absolute_url(self):
		return ('category', None, {
				'category': self.slug
			})
	get_absolute_url = models.permalink(get_absolute_url)








