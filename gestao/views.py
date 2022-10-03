from django.shortcuts import render
from core.models import Categoria, Produto


def gestao_home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'gestao_home.html', {'categorias': categorias, 'produtos': produtos})
