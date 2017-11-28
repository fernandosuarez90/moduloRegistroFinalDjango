# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from album.models import Categoria, Producto, Cliente, Venta
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')


from django.contrib import admin


# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)



