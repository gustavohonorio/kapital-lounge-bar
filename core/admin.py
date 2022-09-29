from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
