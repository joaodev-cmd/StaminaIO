from django import forms
from .models import Aluno, Funcionario,Pagamento

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class PagamentoForm(forms.ModelForm):
    VALORES_PAGAMENTO = [
        (60, 'R$ 60,00'),
        (180, 'R$ 180,00'),
        (360, 'R$ 360,00'),
    ]
    
    valor = forms.ChoiceField(choices=VALORES_PAGAMENTO, label="Valor do Pagamento", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pagamento
        fields = ['aluno', 'valor']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
        }