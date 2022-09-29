from django.shortcuts import render
from .models import Categoria, Produto


def cardapio(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'cardapio.html', {'categorias': categorias, 'produtos': produtos})
