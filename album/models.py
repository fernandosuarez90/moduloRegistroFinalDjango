# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.

class Category(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name 

class Photo(models.Model):
    """ Fotos del album """
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)
    def get_absolute_url(self):
        return reverse('photo-list')
    
    def __unicode__(self):
        return self.title

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)

class Categoria(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('categoria-list')
    def __str__(self):
    	return self.nombre


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/')
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('producto-list')
    def __str__(self):
    	return self.nombre
    
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    celular = models.BigIntegerField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('cliente-list')
    def __str__(self):
        return self.nombre     

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    cantidad_venta = models.BigIntegerField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)
    fecha_venta = models.DateField(blank=True, null=True)
    productos= models.ManyToManyField(Producto)
    
    def get_absolute_url(self):
        return reverse ('venta-list')
    def __str__(self):
        return (self.id_venta)    
        


