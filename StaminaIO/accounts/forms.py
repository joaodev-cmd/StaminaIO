from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
  class Meta:
    model = Usuario
    fields = ['nome', 'email', 'cpf', 'username', 'password1', 'password2']