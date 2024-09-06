from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'quantidade', 'status', 'descricao']

    status = forms.ChoiceField(choices=[])  # Inicialmente vazio, preenchido no __init__

    def __init__(self, *args, **kwargs):
        super(EquipamentoForm, self).__init__(*args, **kwargs)

        # Se o formulário foi submetido, tenta obter o valor de 'quantidade'
        if 'quantidade' in self.data:
            try:
                quantidade = int(self.data.get('quantidade'))  # Pega a quantidade enviada no POST
            except (ValueError, TypeError):
                quantidade = 0  # Define um valor padrão se a quantidade for inválida
        elif self.instance and self.instance.pk:
            # Se estamos editando uma instância existente, usa a quantidade da instância
            quantidade = self.instance.quantidade
        else:
            quantidade = 0  # Valor padrão para novos formulários, antes de definir a quantidade

        # Gera as opções dinâmicas com base na quantidade de equipamentos
        status_choices = [
            (f"{i} Ativos - {quantidade - i} Manutenção", f"{i} Ativos - {quantidade - i} Manutenção")
            for i in range(quantidade + 1)  # Gera opções de 0 até o valor da quantidade
        ]

        # Atualiza o campo `status` com as opções dinâmicas
        self.fields['status'].choices = status_choices
