from django.db import models

from django.db import models

class Suplemento(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data_validade = models.DateField()
    preco = models.FloatField()

    def __str__(self):
        return self.nome
