from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('index')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/equipamentos/', include('equipamento.urls')),
    path('api/pessoa/', include('pessoa.urls')),
    path('api/suplementos/', include('suplemento.urls')),
]
