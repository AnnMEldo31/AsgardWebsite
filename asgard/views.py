from unicodedata import name
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
    l = Item.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'obj': l,
    }
    return HttpResponse(template.render(context, request))


