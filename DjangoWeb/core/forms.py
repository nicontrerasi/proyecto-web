from django import forms
from django.forms import ModelForm
from .models import registro_usuario

class UserForm(ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    mail = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta: 
        model=registro_usuario
        fields=['username','mail','password']
