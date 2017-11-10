from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from tarefas.models import Tarefas

def hello(request):
    return HttpResponse('Olá mundo2!')

def adicionar():
    tarefa = Tarefas()
    tarefa.nome = "teste2222"
    tarefa.descricao = "test2"
    tarefa.save()

def task(request):
    adicionar()  
    print(Tarefas.objects.all())  
    return HttpResponse('Olá tarefas!') 
