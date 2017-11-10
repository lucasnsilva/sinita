from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from tarefas.models import Tarefas

def hello(request):
    return HttpResponse('Olá mundo2! teste')

def adicionar(nome, descricao):
    """Essa função salva a tarefa no banco de dados"""
    # Instância da classe Tarefas
    tarefa = Tarefas()
    tarefa.nome = nome
    tarefa.descricao = descricao
    tarefa.save()

def task(request):   
    """Essa função lista as tarefas e manda os dados para salvar"""  
    # lista de tarefas 'SELECT * FROM TAREFAS'
    lista_tarefas = Tarefas.objects.all()
    # Contador da tabela
    contador = len(lista_tarefas)
    # Requisição POST, responsavel por enviar os dados para a funcao adicionar
    # e execultar a ação de salvar
    if request.method == "POST":
        # Chamando o adicionar e passando as informações da tela
        adicionar(request.POST['nome'], request.POST['descricao'])
        # Redirecionando
        return HttpResponseRedirect('/tarefas')
    # Chamando a tela em HTML
    return render(request, "tarefas.html", locals()) 
