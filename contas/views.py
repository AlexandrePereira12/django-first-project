from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s. <br> <button>Clique aqui</button></body></html>" % now

    return render(request, 'contas/home.html')
