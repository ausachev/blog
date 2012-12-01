#coding=utf-8

from mysite.weblog.models import BolgPost
from django.http import HttpResponse,Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.generic import View 
from mysite.settings import MEDIA_ROOT,MEDIA_URL,STATIC_URL,STATIC_ROOT
def index(request):
	posts = BolgPost.objects.filter(status=2)
	return render_to_response('weblog.html',
		{'posts':posts,'MEDIA_URL':MEDIA_URL,})

def archive(request,year,month,day,slug):
	if slug:
		post = BolgPost.objects.get(slug = slug,status=2)
		return render_to_response('blog_page.html',
			{'post':post,})
	else :
		return HttpResponse(' wrong')
def base(request):
	return render_to_response('base.html',{'STATIC_URL':STATIC_URL,'path':STATIC_ROOT},)



class ViewObject(View):
	"""docstring for ViewObject"""
	def mod_head(self):
		pass
	def mod_foot(self):
		pass
	def mod_content(self):
		pass
	def make(self,template,context):
		pass







