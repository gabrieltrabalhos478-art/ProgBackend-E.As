from django import forms
from .models import Produto


# Formulário baseado no modelo Produto (ModelForm)
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'validade']
        labels = {
            'nome': 'Nome do produto',
            'descricao': 'Descrição',
            'preco': 'Preço (R$)',
            'validade': 'Data de validade',
        }
        widgets = {
            # Usa o seletor de data padrão do HTML5
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }
