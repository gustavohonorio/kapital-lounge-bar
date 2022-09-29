from django.db import models


class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField(blank=False, null=False)
    dt_create = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField(blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    preco = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
