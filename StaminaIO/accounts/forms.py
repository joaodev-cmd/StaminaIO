from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'username', 'password1', 'password2']
        labels = {
            'nome': ('Nome Completo'),
            'email': ('E-mail'),
            'cpf': ('CPF'),
            'username': ('Nome de Usuário'),
            'password1': ('Senha'),
            'password2': ('Confirme a Senha'),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            if field_name == 'password1':
                self.fields[field_name].label = ('Senha')
            elif field_name == 'password2':
                self.fields[field_name].label = ('Confirme a Senha')
