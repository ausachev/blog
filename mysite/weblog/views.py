#coding=utf-8

from mysite.weblog.models import BolgPost
from django.http import HttpResponse,Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from mysite.settings import MEDIA_ROOT,MEDIA_URL

def home(request):
	posts = BolgPost.objects.all()
	return render_to_response('weblog.html',
		{'posts':posts,'MEDIA_URL':MEDIA_URL,})

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = BolgPost.objects.filter(title__icontains=q)
		# message = 'You searched for: %r' % request.GET['q']
		return render_to_response('search_result.html',{'posts':posts,'query':q})
	else :
		message = 'sorry,please input target'
		return HttpResponse(message)
def archive(request,year,month,day,slug):
	if slug:
		post = BolgPost.objects.get(slug = slug)
		return render_to_response('blog_page.html',
			{'post':post,})
	else :
		return HttpResponse(' wrong')

