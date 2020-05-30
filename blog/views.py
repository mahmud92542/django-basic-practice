from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

#import all from models
from .models import *

def BlogDetails(request):
	blogs = Blog.objects.order_by('-date')[:5]
	context = {'blogs':blogs}
	return render (request,'index.html',context)

def whole_blog(request):
	blogs = Blog.objects.order_by('-date')
	paginator = Paginator(blogs, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'blogs':page_obj
	}
	return render (request,'allblog.html',context)

def detail(request, blog_id):
	blog = get_object_or_404(Blog,pk=blog_id) 
	return render (request,'detail.html',{
	'blog':blog
	})