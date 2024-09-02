from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Aluno, Funcionario
from .forms import AlunoForm, FuncionarioForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Aluno, Pagamento
from .forms import PagamentoForm


@login_required
def listar_alunos(request):
    query = request.GET.get('q')
    if query:
        alunos = Aluno.objects.filter(nome__icontains=query)
    else:
        alunos = Aluno.objects.all()

    return render(request, 'pessoa/listar_alunos.html', {'alunos': alunos})

@login_required
def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno adicionado com sucesso!')
            return redirect('pessoa:listar_alunos')
        else:
            messages.error(request, 'Erro ao adicionar aluno. Verifique os dados e tente novamente.')
    else:
        form = AlunoForm()
    return render(request, 'pessoa/form_aluno.html', {'form': form})

@login_required
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('pessoa:listar_alunos')
        else:
            messages.error(request, 'Erro ao atualizar aluno. Verifique os dados e tente novamente.')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'pessoa/form_aluno.html', {'form': form})

@login_required
def deletar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno deletado com sucesso!')
        return redirect('pessoa:listar_alunos')
    return render(request, 'pessoa/confirmar_deletar.html', {'object': aluno})

@login_required# Views para Funcionario
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'pessoa/listar_funcionarios.html', {'funcionarios': funcionarios})

@login_required
def adicionar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário adicionado com sucesso!')
            return redirect('pessoa:listar_funcionarios')
        else:
            messages.error(request, 'Erro ao adicionar funcionário. Verifique os dados e tente novamente.')
    else:
        form = FuncionarioForm()
    return render(request, 'pessoa/form_funcionario.html', {'form': form})

@login_required
def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('pessoa:listar_funcionarios')
        else:
            messages.error(request, 'Erro ao atualizar funcionário. Verifique os dados e tente novamente.')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'pessoa/form_funcionario.html', {'form': form})

@login_required
def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, 'Funcionário deletado com sucesso!')
        return redirect('pessoa:listar_funcionarios')
    return render(request, 'pessoa/confirmar_deletar.html', {'object': funcionario})


def pagar_mensalidade(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.aluno = aluno  # associar o pagamento ao aluno
            pagamento.data_pagamento = timezone.now()
            pagamento.save()
            messages.success(request, 'Mensalidade paga com sucesso!')
            return redirect('pessoa:listar_alunos')
        else:
            messages.error(request, 'Erro ao pagar a mensalidade. Verifique os dados e tente novamente.')
    else:
        form = PagamentoForm(initial={'aluno': aluno})
    return render(request, 'pessoa/form_pagamento.html', {'form': form, 'aluno': aluno})

@login_required
def selecionar_aluno_pagamentos(request):
    # Obtém o parâmetro de busca do nome
    nome = request.GET.get('nome', '')

    # Filtra alunos com base no nome fornecido
    alunos = Aluno.objects.filter(nome__icontains=nome)

    return render(request, 'pessoa/selecionar_aluno_pagamentos.html', {'alunos': alunos})


@login_required
def listar_pagamentos_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    pagamentos = Pagamento.objects.filter(aluno=aluno)

    # Adiciona filtros por valor
    min_valor = request.GET.get('min_valor')
    max_valor = request.GET.get('max_valor')

    if min_valor:
        pagamentos = pagamentos.filter(valor__gte=min_valor)
    if max_valor:
        pagamentos = pagamentos.filter(valor__lte=max_valor)

    return render(request, 'pessoa/listar_pagamentos.html', {'aluno': aluno, 'pagamentos': pagamentos})