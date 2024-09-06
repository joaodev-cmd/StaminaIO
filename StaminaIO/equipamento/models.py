from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)  # Define um valor padrão para quantidade
    status = models.CharField(max_length=100)  # O status será definido dinamicamente no formulário
    descricao = models.CharField(max_length=100)
