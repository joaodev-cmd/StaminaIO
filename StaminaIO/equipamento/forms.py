from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'quantidade', 'status', 'descricao']  # Incluindo todos os campos do modelo
