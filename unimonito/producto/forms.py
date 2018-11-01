from django import forms

class getClienteFORM(forms.Form):
    nombre_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nombreUsuario', 'placeholder':'Nombre'}))
    cedula_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cedulaUsuario', 'placeholder':'Cedula'}))
    ciudad_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'ciudadUsuario', 'placeholder':'Ciudad'}))
