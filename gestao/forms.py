from django import forms
from core.models import Produto, Categoria


class ProdutoForm(forms.ModelForm):
    categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    preco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_novo = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco']

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs['readonly'] = True
        self.fields['categoria'].required = False
        self.fields['id'].required = False
        self.fields['nome'].required = False
        self.fields['descricao'].required = False
        self.fields['preco'].required = False
        self.fields['is_novo'].required = False
