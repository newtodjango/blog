from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from . import service

import pyshorteners

def shorten(request,url):
    shortened_url = request.build_absolute_uri(reverse('redirect',args=[shortened_url_hash]))
    shortened_url_hash = service.shorten(url)
    return render(request,'main/link.html', {'shortened_url':shortened_url})


def index(request):
    return render(request,'main/index.html')


def shorten_post(request):
    return shorten(request,request.POST['url'])


def redirect_hash(request,url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)
