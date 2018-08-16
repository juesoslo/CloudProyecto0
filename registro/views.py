from django.shortcuts import render_to_response, render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from evento.models import Usuario
from registro.forms import RegisterForm, RegisterUsuario
from django.contrib.auth.decorators import login_required


def register_user(request):
	if request.method == 'POST':
		formUser = RegisterForm(request.POST)
		formUsuario = RegisterUsuario(request.POST, request.FILES)
		if formUser.is_valid() and formUsuario.is_valid():
			user = formUser.save()
			user.username = user.email
			user.save()

			usuario = formUsuario.save()
			usuario.user = user
			usuario.save()

			return HttpResponseRedirect('/accounts/login')
		else:
			render(request, 'registro.html', {'formUser' :formUser, 'formUsuario': formUsuario})
	else:
		formUser = RegisterForm()
		formUsuario = RegisterUsuario()
	return render(request, 'registro.html', {'formUser' :formUser, 'formUsuario': formUsuario})


