"""myapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib.auth.decorators import login_required


from django.contrib.auth import views as auth_views

from rest_framework import routers
from album import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'photos', views.PhotoViewSet)


urlpatterns = [


    url(r'^',include(router.urls)),
   
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    #url('', include('social_django.urls', namespace='social')),

    
   
    
    
    
    
    #url(r'^album/', login_required(include('album.urls'))),
    url(r'^admin/', admin.site.urls),
    url(r'^album/', include('album.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')), 


]