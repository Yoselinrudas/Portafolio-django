from django import forms

# Mi formulario
class formularioproyecto(forms.Form):

    Fotos = forms.CharField(max_length = 120)

    Titulos= forms.CharField(max_length = 50)

    Descripciones = forms.CharField(max_length = 80)

    Tags = forms.CharField(max_length = 50)

    URL_GIT = forms.CharField(max_length = 150)