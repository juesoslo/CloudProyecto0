from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from modelos.models import Usuario, Ciudad, Pais
from registro.forms import RegisterForm, RegisterUsuario
from django.contrib.auth.decorators import login_required


def register_user(request):
	if request.method == 'POST':
		formUser = RegisterForm(request.POST)
		formUsuario = RegisterUsuario(request.POST, request.FILES)
		if formUser.is_valid() and formUsuario.is_valid():
			user = formUser.save()
			usuario = formUsuario.save()
			usuario.user = user
			usuario.save()

			return HttpResponseRedirect('/accounts/login')
	else:
		formUser = RegisterForm()
		formUsuario = RegisterUsuario()
	return render(request, 'registro.html', {'formUser' :formUser, 'formUsuario': formUsuario})
## line 28, 30, 31 form to formUpdate y instance usuario a instance user
@login_required
def update_usuario(request):
	loggedUser = request.user
	usuario = Usuario.objects.get(user=loggedUser.id)
	form = RegisterUsuario(request.POST or None,request.FILES or None, instance=usuario)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/especies')
	return render(request, 'updateRegistro.html', {'form': form})
