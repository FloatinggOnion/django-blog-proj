from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from . models import page

# Create your views here.

def index(request):
    #return HttpResponse("<h1>JP's Blog Site</h1>")
    return render(request, 'base.html')

def about(request):
    '''temp = loader.get_template('about.html')
    return HttpResponse(temp.render({}, request))
'''
    return render(request, 'pages/about.html')


def quickreads(request):
     return render(request, 'pages/quick_reads.html')