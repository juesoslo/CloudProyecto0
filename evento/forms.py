from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from evento.models import Evento


class RegisterEvento(ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_final', 'presencial', 'usuario', 'fecha_registro')
        exclude = ('usuario','fecha_registro',)

class UpdateEvento(ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_final', 'presencial', 'usuario', 'fecha_registro')
        exclude = ('usuario','fecha_registro',)

class ListEvento(ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_final', 'presencial', 'usuario', 'fecha_registro')
        exclude = ('usuario','fecha_registro',)

class DetailsEvento(ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_final', 'presencial', 'usuario', 'fecha_registro')
        exclude = ('usuario','fecha_registro',)
