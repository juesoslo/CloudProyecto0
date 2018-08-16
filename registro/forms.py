from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from evento.models import Usuario


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        exclude = ('username',)


class RegisterUsuario(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('user',)


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
