from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader

def index(request):
    
    return HttpResponse('Index view')

def categories(request):
    cats = Categories.objects.all()
    template = loader.get_template('store.html')
    context = {
        'categories_list':cats
    }
    return HttpResponse(template.render(context, request))

def products(request, id):
    cats = Product.objects.filter(category_id=id)
    template = loader.get_template('pd.html')
    context = {
        'categories_list':cats
    }
    return HttpResponse(template.render(context, request))


