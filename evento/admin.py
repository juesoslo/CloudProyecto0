from django.contrib import admin
from .models import Categoria, Usuario, Evento

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Evento)