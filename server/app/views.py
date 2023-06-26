from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SANPHAM
# Create your views here.
def HOME(request):
    templates = loader.get_template('home.html')
    return HttpResponse(templates.render())


def Login(request):
    templates = loader.get_template('login.html')
    return HttpResponse(templates.render())

def Register(request):
    templates = loader.get_template('register.html')
    return HttpResponse(templates.render())

def ShowProduct(request):
    #get 
    sp = SANPHAM.objects.all().values()
    # filter 
    # sp = SANPHAM.objects.filter(TenSP__startswith = 'A').values
    template = loader.get_template('product.html')
    context = {
        'sp':sp,
    }
    return HttpResponse(template.render(context,request))

