from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .models import Transacao
from .forms import TransacaoForm


def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']

    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s. <br> <button>Clique aqui</button></body></html>" % now

    return render(request, 'contas/home.html', data)

def listagem(request):
    data={}

    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)

def novaTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None,instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    data['transacao'] = transacao

    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('listagem')