from django.conf.urls import url
from album import views

from django.contrib.auth.decorators import login_required



urlpatterns = [
     url(r'^$',login_required ( views.base), name='base'), 
    
    
     #-------------categoria---------------------#
	url(r'^$', views.base, name='base'),
	url(r'^categoria/$', views.CategoriaListView.as_view(), name='categoria-list'),
	url(r'^categoria/(?P<pk>[0-9]+)/detail/$', views.CategoriaDetailView.as_view(), name='categoria-detail'),
	
	url(r'^categoria/(?P<pk>[0-9]+)/update/$', views.CategoriaUpdate.as_view(), name='categoria-update'),
	url(r'^categoria/(?P<pk>[0-9]+)/delete/$', views.CategoriaDelete.as_view(), name='categoria-delete'),
	url(r'^categoria/create/$', views.CategoriaCreate.as_view(), name='categoria-create'),

	#----------productos----------------------#

	url(r'^producto/$', views.ProductoListView.as_view(), name='producto-list'),
	url(r'^producto/(?P<pk>[0-9]+)/detail/$', views.ProductoDetailView.as_view(), name='producto-detail'),
	
	url(r'^producto/(?P<pk>[0-9]+)/update/$', views.ProductoUpdate.as_view(), name='producto-update'),
	url(r'^producto/(?P<pk>[0-9]+)/delete/$', views.ProductoDelete.as_view(), name='producto-delete'),
	url(r'^producto/create/$', views.ProductoCreate.as_view(), name='producto-create'),


	#------------cliente----------------------#

	url(r'^cliente/$', views.ClienteListView.as_view(), name='cliente-list'),
	url(r'^cliente/(?P<pk>[0-9]+)/detail/$', views.ClienteDetailView.as_view(), name='cliente-detail'),

	url(r'^cliente/(?P<pk>[0-9]+)/update/$', views.ClienteUpdate.as_view(), name='cliente-update'),
	url(r'^cliente/(?P<pk>[0-9]+)/delete/$', views.ClienteDelete.as_view(), name='cliente-delete'),
	url(r'^cliente/create/$', views.ClienteCreate.as_view(), name='cliente-create'),

	#----------venta-------------------------#

	url(r'^venta/$', views.VentaListView.as_view(), name='venta-list'),
	url(r'^venta/(?P<pk>[0-9]+)/detail/$', views.VentaDetailView.as_view(), name='venta-detail'),
	url(r'^venta/(?P<pk>[0-9]+)/delete/$', views.VentaDelete.as_view(), name='venta-delete'),
	url(r'^venta/create/$', views.VentaCreate.as_view(), name='venta-create'),

	
     

     
    # Update
    url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(),name='photo-update'),
    #Create
    url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
    #Delete
    url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(),name='photo-delete'),
]