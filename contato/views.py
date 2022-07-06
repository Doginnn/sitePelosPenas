from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from .forms import ContatoForm
from .forms import ContactForm


def index(request):
    count = User.objects.count()
    return render(request, 'index.html', {"count": count})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Consulta ao site"
            body = {
                'nome': form.cleaned_data['nome'],
                'email': form.cleaned_data['email'],
                'titulo': form.cleaned_data['titulo'],
                'menssagem': form.cleaned_data['menssagem'],
            }
            message = "\n" . join(body.values())

            try:
                send_mail(subject, message, 'contatopelosepenas@gmail.com', ['contatopelosepenas@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Cabeçalho inválido!')
            return redirect("index.html")

    form = ContactForm()
    return render(request, 'parciais/_formContato.html', {'form': form})


# def contato(request):
#     if request.method == 'POST':
#         form = ContatoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'index.html')
#     form = ContatoForm()
#     context = {'form': form}
#     return render(request, 'parciais/_formContato.html', context)

# class ContactView(CreateView):
#     form_class = ContatoForm
#     success_url = reverse_lazy('contact')
#     template_name = 'contato/_formContato.html'
#
#
# def form_invalid(self, form):
#     http_header = self.request.META
#     send_email(form, http_header)
#     messages.error(self.request, 'Algo inesperado aconteceu. Tente novamente!')
#     return HttpResponseRedirect('index')
#
#
# def form_valid(self, form):
#     http_header = self.request.META
#     send_email(form, http_header)
#     messages.success(self.request, 'Menssagem enviada com sucesso!')
#     return super().form_valid(form)
#
#
# def send_email(form_data, http_header):
#     try:
#         if http_header.get('HTTP_X_REAL_IP'):
#             remote_ip = http_header.get('HTTP_X_REAL_IP')
#         elif http_header.get('X-FORWARDED-FOR'):
#             http_header.get('X-FORWARDED-FOR')
#         else:
#             remote_ip = 'Não foi possível buscar o endereço IP do cliente!'
#     except:
#         pass
#
#     form_message = form_data.cleaned_data['menssagem']
#     subject = form_data.cleaned_data['titulo']
#
#     try:
#         email = form_data.cleaned_data['email']
#     except:
#         email = 'E-mail inválido!'
#
#     message = f'''A menssagem foi recebida de {email} com IP: {remote_ip}
#
#     {form_message}
#     '''
#
#     send_mail(subject,
#               message,
#               from_email=settings.EMAIL_HOST_USER,
#               recipient_list=[settings.ADMIN_EMAIL],
#               fail_silently=False)
