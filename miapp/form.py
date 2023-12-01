from django import forms 

class CrearNuevaTarea(forms.Form):
    titulo = forms.CharField(label="Titulo de la tarea",max_length=200,widget=forms.TextInput(attrs={'class':'input','style':'width:50%;'}))
    descripcion = forms.CharField(label="Descripción  de la tarea",widget=forms.Textarea(attrs={'class':'textarea','style':'width:50%'}))

class CrearNuevoProyecto(forms.Form):
    name = forms.CharField(label="Nombre del proyecto",max_length=200,widget=forms.TextInput(attrs={'class':'input','style':'width:60%'}))
