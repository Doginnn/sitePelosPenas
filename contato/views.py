from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    count = User.objects.count()
    return render(request, 'index.html', {"count": count})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'parciais/_formContato.html')
    form = ContatoForm()
    context = {'form': form}
    return render(request, 'parciais/_formContato.html', context)
