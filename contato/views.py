from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    count = User.objects.count()
    return render(request, 'index.html', {"count": count})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        send_mail(
            ContatoForm.nome,
            ContatoForm.email,
            ContatoForm.titulo,
            ContatoForm.menssagem
        )

        if form.is_valid():
            form.save()
            return render(request, 'parciais/_formContato.html')
    form = ContatoForm()
    context = {'form': form}
    return render(request, 'index.html', context)
