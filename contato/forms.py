from django import forms
from django.forms import ModelForm
from .models import Contato

class ContactForm(forms.form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=75)
    titulo = forms.CharField(max_length=100)
    menssagem = forms.TextField(widget=forms.Textarea, max_length=2000)

# class ContatoForm(ModelForm):
#     class Meta:
#         model = Contato
#         fields = '__all__'
