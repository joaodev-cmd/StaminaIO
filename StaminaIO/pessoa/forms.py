from django import forms
from .models import Aluno, Funcionario, Pagamento

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
        (80, 'Plano Mensal - R$ 80,00'),
        (225, 'Plano Trismestral - R$ 225,00'),
        (420, 'Plano Semestral - R$ 420,00'),
        (780, 'Plano Anual - R$780,00'),
    ]
    
    valor = forms.ChoiceField(choices=VALORES_PAGAMENTO, label="Valor do Pagamento", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pagamento
        fields = ['aluno', 'valor']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
        }
        
class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Digite sua senha para confirmar')
