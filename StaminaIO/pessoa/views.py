from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Aluno, Funcionario
from .forms import AlunoForm, FuncionarioForm

# Views para Aluno
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'pessoa/listar_alunos.html', {'alunos': alunos})

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

def deletar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno deletado com sucesso!')
        return redirect('pessoa:listar_alunos')
    return render(request, 'pessoa/confirmar_deletar.html', {'object': aluno})

# Views para Funcionario
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'pessoa/listar_funcionarios.html', {'funcionarios': funcionarios})

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

def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, 'Funcionário deletado com sucesso!')
        return redirect('pessoa:listar_funcionarios')
    return render(request, 'pessoa/confirmar_deletar.html', {'object': funcionario})
