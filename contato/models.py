from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    titulo = models.CharField(max_length=100)
    menssagem = models.TextField(max_length=256)

    def __str__(self):
        return self.titulo, self.email, self.nome
