from django.shortcuts import render , get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.utils.text import slugify
from .models import New

# Create your views here.

def news(request):

    news = New.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        "news": news,
    }
    return HttpResponse(template.render(context, request))

def newDetail(request,title):
    the_title = title.replace("-"," ")
    new = New.objects.get(title=title)
    template = loader.get_template('newdetail.html')
    context = {
        'new': new
    }

    return HttpResponse(template.render(context, request))