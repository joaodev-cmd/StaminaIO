from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .serializers import SuplementoSerializer
from .models import Suplemento
from .forms import SuplementoForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def listar_suplementos(request):
    suplementos = Suplemento.objects.all()
    return render(request, 'suplemento/listar_suplementos.html', {'suplementos': suplementos})

@login_required
def adicionar_suplemento(request):
    if request.method == 'POST':
        form = SuplementoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Suplemento adicionado com sucesso!')
            return redirect('suplemento:listar_suplementos')
        else:
            messages.error(request, 'Erro ao adicionar suplemento. Verifique os dados e tente novamente.')
    else:
        form = SuplementoForm()
    return render(request, 'suplemento/form_suplemento.html', {'form': form})

@login_required
def editar_suplemento(request, pk):
    suplemento = get_object_or_404(Suplemento, pk=pk)
    if request.method == 'POST':
        form = SuplementoForm(request.POST, instance=suplemento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Suplemento atualizado com sucesso!')
            return redirect('suplemento:listar_suplementos')
        else:
            messages.error(request, 'Erro ao atualizar suplemento. Verifique os dados e tente novamente.')
    else:
        form = SuplementoForm(instance=suplemento)
    return render(request, 'suplemento/form_suplemento.html', {'form': form})

@login_required
def deletar_suplemento(request, pk):
    suplemento = get_object_or_404(Suplemento, pk=pk)
    if request.method == 'POST':
        suplemento.delete()
        messages.success(request, 'Suplemento deletado com sucesso!')
        return redirect('suplemento:listar_suplementos')
    return render(request, 'suplemento/confirmar_deletar.html', {'object': suplemento})

class SuplementoViewSet(viewsets.ModelViewSet):
    queryset = Suplemento.objects.all()
    serializer_class = SuplementoSerializer
    permission_classes = [IsAuthenticated] 