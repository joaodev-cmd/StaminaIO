from .models import Equipamento
from .serializers import EquipamentoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Equipamento
from .forms import EquipamentoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

@login_required
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/listar_equipamentos.html', {'equipamentos': equipamentos})

@login_required
def adicionar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento adicionado com sucesso!')
            return redirect('equipamento:listar_equipamentos')
        else:
            messages.error(request, 'Erro ao adicionar equipamento. Verifique os dados e tente novamente.')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/form_equipamento.html', {'form': form})

@login_required
def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('equipamento:listar_equipamentos')
        else:
            messages.error(request, 'Erro ao atualizar equipamento. Verifique os dados e tente novamente.')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/form_equipamento.html', {'form': form})

@login_required
def deletar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento deletado com sucesso!')
        return redirect('equipamento:listar_equipamentos')
    return render(request, 'equipamento/confirmar_deletar.html', {'object': equipamento})

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    permission_classes = [IsAuthenticated]  # 🔒 Protege a API


