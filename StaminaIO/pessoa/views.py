from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Aluno, Funcionario, Pagamento
from .forms import AlunoForm, FuncionarioForm, PagamentoForm, ConfirmPasswordForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import AlunoSerializer, FuncionarioSerializer, PagamentoSerializer

# Views para Alunos
@login_required
def listar_alunos(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')
    
    alunos = Aluno.objects.all()

    if query:
        alunos = alunos.filter(nome__icontains=query)
    if status_filter:
        alunos = alunos.filter(status=status_filter)

    return render(request, 'pessoa/listar_alunos.html', {'alunos': alunos, 'status_filter': status_filter})

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

# Views para Funcionários
@login_required
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

# Views para Pagamentos
@login_required
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
    nome = request.GET.get('nome', '')
    alunos = Aluno.objects.filter(nome__icontains=nome)
    return render(request, 'pessoa/selecionar_aluno_pagamentos.html', {'alunos': alunos})

@login_required
def listar_pagamentos_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    pagamentos = Pagamento.objects.filter(aluno=aluno)
    
    min_valor = request.GET.get('min_valor')
    max_valor = request.GET.get('max_valor')

    if min_valor:
        pagamentos = pagamentos.filter(valor__gte=min_valor)
    if max_valor:
        pagamentos = pagamentos.filter(valor__lte=max_valor)

    return render(request, 'pessoa/listar_pagamentos.html', {'aluno': aluno, 'pagamentos': pagamentos})

@login_required
def deletar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id)
    aluno = pagamento.aluno

    if request.method == 'POST':
        form = ConfirmPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if request.user.check_password(password):
                pagamento.delete()
                messages.success(request, 'Pagamento deletado com sucesso!')
                return redirect('pessoa:listar_pagamentos_aluno', aluno_id=aluno.id)
            else:
                messages.error(request, 'Senha incorreta. Tente novamente.')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados e tente novamente.')
    else:
        form = ConfirmPasswordForm()

    return render(request, 'pessoa/confirmar_delecao_pagamento.html', {'pagamento': pagamento, 'form': form})

# ViewSets para APIs
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [IsAuthenticated]
