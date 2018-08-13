# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	# (Conferencia, Seminario, Congreso, Curso)
	
	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'

	def __str__(self):
		return '%s' % (self.nombre)

	def __unicode__(self):
		return self.nombre

class Usuario(models.Model):
	user = models.OneToOneField(User)
	nombre = models.CharField(max_length=100, default="")
	apellido = models.CharField(max_length=100, default="")

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return '%s' % (self.user.username)

class Evento(models.Model):
	nombre			= models.CharField(max_length=100)
	categoria		= models.ForeignKey(Categoria)
	lugar			= models.CharField(max_length=100)
	direccion		= models.CharField(max_length=100)
	fecha_inicio	= models.DateTimeField(  null=True,default=datetime.now(), blank=True )
	fecha_final		= models.DateTimeField(  null=True,default=datetime.now(), blank=True )
	presencial		= models.BooleanField(default=True)
	usuario			= models.ForeignKey(Usuario)

	class Meta:
		verbose_name = 'Evento'
		verbose_name_plural = 'Eventos'

	def __str__(self):
		return '%s' % (self.nombre)

	def __unicode__(self):
		return self.nombre