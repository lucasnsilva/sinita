from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def hello(request):
    return HttpResponse('Olá mundo!')
