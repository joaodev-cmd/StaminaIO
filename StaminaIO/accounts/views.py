from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from .forms import UsuarioForm

def createusu(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UsuarioForm()
        return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login') 
