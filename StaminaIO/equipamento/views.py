from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm

# View para listar todos os equipamentos
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/listar_equipamentos.html', {'equipamentos': equipamentos})

# View para adicionar um novo equipamento
def adicionar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/form_equipamento.html', {'form': form})

# View para editar um equipamento existente
def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/form_equipamento.html', {'form': form})

# View para deletar um equipamento
def deletar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_equipamentos')
    return render(request, 'equipamento/confirmar_deletar.html', {'object': equipamento})
