from django.shortcuts import render
from pessoa.models import Aluno, Funcionario
from equipamento.models import Equipamento
from suplemento.models import Suplemento

def index(request):
    total_alunos = Aluno.objects.count()
    total_funcionarios = Funcionario.objects.count()
    total_equipamentos = Equipamento.objects.count()
    total_suplementos = Suplemento.objects.count()

    context = {
        'total_alunos': total_alunos,
        'total_funcionarios': total_funcionarios,
        'total_equipamentos': total_equipamentos,
        'total_suplementos': total_suplementos,
    }

    return render(request, 'dashboard/index.html', context)
