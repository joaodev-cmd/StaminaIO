from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()

    class Meta:
        abstract = True

class Aluno(Pessoa):
    peso = models.FloatField()
    endereco = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15)
    altura = models.FloatField()
    plano = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    funcao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    horas_trabalhadas = models.IntegerField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
