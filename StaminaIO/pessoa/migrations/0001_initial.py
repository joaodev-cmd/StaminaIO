# Generated by Django 5.0.4 on 2024-08-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('idade', models.IntegerField()),
                ('peso', models.FloatField()),
                ('endereco', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('telefone', models.CharField(max_length=15)),
                ('altura', models.FloatField()),
                ('plano', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('idade', models.IntegerField()),
                ('funcao', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horas_trabalhadas', models.IntegerField()),
                ('telefone', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]