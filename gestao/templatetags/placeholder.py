from django.template import Library

'''
CRIANDO UMA TAG (METODO) PERSONALIZADO
PARA ALTERAR O PLACEHOLDER
DOS INPUTS DOS MODEL FORMS
'''

register = Library()


def placeholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value


register.filter(placeholder)
