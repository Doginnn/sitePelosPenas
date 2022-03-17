from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    count = User.objects.count()
    return render(request, 'index.html', {"count": count})


def contato(request):
    form = ContatoForm()
    context = {'form': form}
    return render(request, 'contato/contato.html', context)
