from django.db import models

class Suplemento(models.Model):
    nome = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100, default="")
    preco = models.FloatField()
    quantidade = models.IntegerField(default=1)