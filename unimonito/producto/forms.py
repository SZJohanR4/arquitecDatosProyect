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

class nuevaRecetaForm(forms.Form):
    nombre_Receta=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nombreReceta', 'placeholder':'Nombre'}))
    ingrediente1=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'ingrediente1', 'placeholder':'Ingrediente'}))
    cantidad1=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cantidad1', 'placeholder':'Cantidad'}))
    ingrediente2=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'ingrediente2', 'placeholder':'Ingrediente'}))
    cantidad2=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cantidad2', 'placeholder':'Cantidad'}))
    ingrediente3=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'ingrediente3', 'placeholder':'Ingrediente'}))
    cantidad3=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cantidad3', 'placeholder':'Cantidad'}))
    preparacion=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'preparacion', 'placeholder':'Preparacion'}))
