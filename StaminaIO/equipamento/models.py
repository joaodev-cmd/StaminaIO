from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)  # Definindo um valor padrão para quantidade
    status = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)  # Nome do campo corrigido para seguir a convenção de nomenclatura
