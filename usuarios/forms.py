from django import forms

class UsuarioValidate(forms.Form):
	nome = forms.CharField(max_length=50, required=True)