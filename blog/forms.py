from django import forms
import datetime
class PostFormulario(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=45678912)
    date = forms.CharField(max_length=4565)
