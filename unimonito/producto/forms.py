from django import forms

class getClienteFORM(forms.Form):
    nombre_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nombreUsuario', 'placeholder':'Nombre'}))
    cedula_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cedulaUsuario', 'placeholder':'Cedula'}))
    ciudad_Usuario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'ciudadUsuario', 'placeholder':'Ciudad'}))

class getProductoFORM(forms.Form):
    nombre_Producto=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nombrProducto', 'placeholder':'Nombre','disabled':'disabled'}))
    fecha_Consumo=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'fechaConsumo', 'placeholder':'Cedula','disabled':'disabled'}))
    observacion=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'observacion', 'placeholder':'Ciudad','disabled':'disabled'}))
    precio=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'precio', 'placeholder':'Ciudad','disabled':'disabled'}))
