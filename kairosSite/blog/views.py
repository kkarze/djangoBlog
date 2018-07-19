# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
# Create your views here.

def index(request):
    #return HttpResponse(u"Welcome to Django.")
    return render(request, 'index.html', {})

def blog_index(request):
    blog_list = Article.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})
