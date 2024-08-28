from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField
    status = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=100)
