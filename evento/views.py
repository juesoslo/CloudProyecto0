from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from evento.models import Evento, Usuario
from django.contrib.auth.models import User
from evento.forms import RegisterEvento, UpdateEvento, ListEvento, DetailsEvento
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
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
			render(request, 'agregar.html', {'formEvento' :formEvento})
	else:
		formEvento = RegisterEvento()
	return render(request, 'agregar.html', {'formEvento' :formEvento})


@login_required
def update_evento(request, id):
	evento = get_object_or_404(Evento, id=id)
	formEvento = UpdateEvento(request.POST or None, instance=evento)

	if request.method == 'POST':
		if formEvento.is_valid():
			usuario = get_object_or_404(Usuario, user=request.user)
			evento = formEvento.save()
			evento.usuario = usuario
			evento.fecha_registro = datetime.now()
			evento.save()
			return HttpResponseRedirect('/evento')
		else:
			return render(request, 'actualizar.html', {'formEvento': formEvento, 'id': id})
	return render(request, 'actualizar.html', {'formEvento': formEvento, 'id': id})


@login_required
def list_evento(request):
	usuario = get_object_or_404(Usuario, user=request.user)
	lista_eventos = Evento.objects.filter(usuario=usuario).order_by('-fecha_registro')
	context = {'lista_eventos': lista_eventos }
	return render(request, 'eventos.html', context)

@login_required
def delete_evento(request, id):
	evento = Evento.objects.filter(id=id).delete()
	return HttpResponseRedirect('/evento')


@login_required
def details_evento(request, id):
	evento = get_object_or_404(Evento, id=id)
	formEvento = DetailsEvento(request.POST or None, instance=evento)
	return render(request, 'details.html', {'formEvento' :formEvento})