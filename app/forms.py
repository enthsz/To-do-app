from .models import Tarefa, CustomUser
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreation(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ('username', 'email','password1','password2')



class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        exclude = ['user']


class LoginForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    senha = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Senha')




