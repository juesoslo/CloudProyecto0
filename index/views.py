from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	#context = {}
	#return render(request, 'index.html', context)
	if( request.user != "" ):
		return HttpResponseRedirect('/evento')
	else:
		return HttpResponseRedirect('/accounts/login')

@login_required
def eventos(request):
	return HttpResponseRedirect('/evento')