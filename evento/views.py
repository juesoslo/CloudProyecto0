from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from evento.models import Evento, Usuario
from django.contrib.auth.models import User
from evento.forms import RegisterEvento, UpdateEvento
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def register_evento(request):
	if request.method == 'POST':
		formEvento = RegisterEvento(request.POST)
		if formEvento.is_valid():
			usuario = get_object_or_404(Usuario, user=request.user)
			evento = formEvento.save()
			evento.usuario = usuario
			evento.fecha_registro = datetime.now()
			evento.save()
			
			return HttpResponseRedirect('/evento')
		else:
			render(request, 'registro.html', {'formEvento' :formEvento})
	else:
		formEvento = RegisterEvento()
	return render(request, 'registro.html', {'formEvento' :formEvento})


def update_evento(request):
	formEvento = UpdateEvento()
	return render(request, 'registro.html', {'formEvento' :formEvento})

def list_evento(request):
	usuario = get_object_or_404(Usuario, user=request.user)
	lista_eventos = Evento.objects.filter(usuario=usuario).order_by('-fecha_registro')
	context = {'lista_eventos': lista_eventos }
	return render(request, 'eventos.html', context)