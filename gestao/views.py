from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Categoria, Produto
from .forms import ProdutoForm


def gestao_home(request):
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            # VALIDANDO INPUTS
            id_p = request.POST.get('id_produto')
            produto_db = Produto.objects.get(id=id_p)
            nome = form_produto.cleaned_data['nome']
            descricao = form_produto.cleaned_data['descricao']
            descricao = descricao if descricao else produto_db.descricao
            preco = form_produto.cleaned_data['preco']
            preco = preco if preco else produto_db.preco
            categoria = Categoria.objects.filter(nome__icontains=str(form_produto.cleaned_data['categoria']))[:1]
            categoria = Categoria.objects.get(id=categoria[0].id)
            is_novo = form_produto.cleaned_data['is_novo']

            # CASO A FLAG DE NOVO PRODUTO ESTEJA ATIVA, CADASTRA UM NOVO PRODUTO
            if 'True' in is_novo:
                novo_produto = Produto(nome=nome, descricao=descricao, preco=preco, categoria=categoria)
                novo_produto.save()
                messages.success(request, 'Produto cadastrado com sucesso.')
                redirect('gestao_home')
            else:
                # ATUALIZANDO PRODUTO
                p = get_object_or_404(Produto, id=id_p)
                form_produto = ProdutoForm(request.POST, instance=p)
                if form_produto.is_valid():
                    p.save()
                    messages.success(request, 'Produto atualizado com sucesso.')
                    redirect('gestao_home')
        else:
            print(form_produto.errors)
            for campo in form_produto:
                if campo.errors:
                    messages.error(request, campo.errors)
                    break

    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    form_produto = ProdutoForm()

    return render(request, 'gestao_home.html', {'categorias': categorias, 'produtos': produtos, 'form_p': form_produto})
