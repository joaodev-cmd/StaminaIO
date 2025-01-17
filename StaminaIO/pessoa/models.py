from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()

    class Meta:
        abstract = True

class Aluno(Pessoa):
    MATRICULADO = 'M'
    NAO_MATRICULADO = 'NM'
    STATUS_CHOICES = [
        (MATRICULADO, 'Matriculado'),
        (NAO_MATRICULADO, 'Não Matriculado'),
    ]
    
    peso = models.FloatField()
    endereco = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=MATRICULADO)
    telefone = models.CharField(max_length=15)
    altura = models.FloatField()

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    funcao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    horas_trabalhadas = models.IntegerField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pagamento de {self.aluno.nome} em {self.data_pagamento}"
