# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from album.models import Category, Photo, Categoria, Producto, Cliente, Venta
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

from rest_framework import viewsets
from album.serializers import CategorySerializer, PhotoSerializer


from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
def first_view(request):
    return HttpResponse('Esta es mi primera vista!')
    
@login_required
def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html', context)

@login_required
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)



class LoginRequireMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequireMixin, cls).as_view())


def base(request):
    return render(request, 'base.html')    

class PhotoListView(LoginRequireMixin, ListView):
    login_required = True
    model = Photo

class PhotoDetailView(LoginRequireMixin, DetailView):
    model = Photo

@login_required
def base(request):
   return render(request, 'base.html')

class PhotoUpdate(LoginRequireMixin, UpdateView):
    model = Photo
    fields='__all__'

class PhotoCreate(LoginRequireMixin, CreateView):
    model = Photo
    fields='__all__'
    

class PhotoDelete(LoginRequireMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')

    

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class PhotoViewSet(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer


#------------------------------------producto------------------------------------

class ProductoListView(ListView):
	model = Producto

class ProductoDetailView(DetailView):
	model = Producto	

class ProductoUpdate(UpdateView):
	model=Producto
	fields='__all__'

class ProductoDelete(DeleteView):
	model=Producto
	success_url=reverse_lazy('producto-list')

class ProductoCreate(CreateView):
	model=Producto
	fields='__all__'
    


#----------------------------------categoria-------------------------------------

class CategoriaListView(ListView):
	model = Categoria


class CategoriaDetailView(DetailView):
	model = Categoria


class CategoriaUpdate(UpdateView):
	model=Categoria
	fields='__all__'

class CategoriaDelete(DeleteView):
	model=Categoria
	success_url=reverse_lazy('categoria-list')

class CategoriaCreate(CreateView):
	model=Categoria
	fields='__all__'

#-----------------------------------Cliente-----------------------------------------
class ClienteListView(ListView):
	model = Cliente

class ClienteDetailView(DetailView):
	model = Cliente

class ClienteUpdate(UpdateView):
	model=Cliente
	fields='__all__'

class ClienteDelete(DeleteView):
	model=Cliente
	success_url=reverse_lazy('cliente-list')

class ClienteCreate(CreateView):
	model=Cliente
	fields='__all__'

#------------------------------------------------------------------------------------


#-----------------------------------Venta-------------------------------------------

class VentaListView(ListView):
	model = Venta


class VentaDetailView(DetailView):
	model = Venta	

class VentaDelete(DeleteView):
	model=Venta
	success_url=reverse_lazy('venta-list')

class VentaCreate(CreateView):
	model=Venta
	fields='__all__'	
#------------------------------------------------------------------------------------

def categoria(request):
	categoria_list = Categoria.objects.all()
	context = {'object_list': categoria_list}
	return render(request, 'tienda/categoria.html', context)


def categoria_detail(request, categoria_id):
	categoria = Categoria.objects.get(id_categoria=categoria_id)
	context = {'object': categoria}
	return render(request, 'tienda/categoria_detail.html', context)    