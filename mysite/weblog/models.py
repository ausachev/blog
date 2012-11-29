#coding=utf-8
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.template.defaultfilters import slugify
import sys,os
from mysite.settings import MEDIA_ROOT
from django.utils import timezone
from django.utils.http import urlquote
# MEDIA_ROOT = '/uploads/image'
# Create your models here.

class BolgPost(models.Model):
	STATUS_CHOICES = (
		(1, ('Draft')),
		(2, ('Public')),)
	title = models.CharField(max_length= 150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	author = models.CharField(max_length= 30,default='GreenTea')
	slug = models.SlugField(unique=True,help_text=("used to build the entry's URL"),
                            max_length=255) 
	images = models.ImageField(('images'), upload_to=MEDIA_ROOT,
                              blank=True ,max_length=1000,help_text=('used for illustration'))
	status = models.IntegerField(('status'), choices=STATUS_CHOICES, default=1)
	
	def save(self, *args, **kwargs):

		if not self.slug:
			# title = urlquote(self.title)
			self.slug = slugify(self.title)
		super(BolgPost,self).save(*args, **kwargs)
			

	@models.permalink
	def get_absolute_url(self):
		timestamp = self.timestamp
		return ('archive',None,{
		'year' : timestamp.strftime('%Y'),
		'month': timestamp.strftime('%m'),
		'day'  : timestamp.strftime('%d'),
		'slug' : self.slug,
		})
	# get_absolute_url = models.permalink(get_absolute_url)

	def __unicode__(self):
		return self.title
class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	class Meta:
		verbose_name        = ('category')
		verbose_name_plural = ('categorys')
		ordering            = ('title',)
		def __unicode__(self):
			return self.title
	@models.permalink
	def get_absolute_url(self):
		return ('category', None, {
				'category': self.slug
			})








