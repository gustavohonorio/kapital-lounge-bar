from django.shortcuts import render


def cardapio(request):
    return render(request, 'cardapio.html', )
