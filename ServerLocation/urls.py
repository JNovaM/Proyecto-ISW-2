"""ServerLocation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  Web import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('salir/',views.salir),
    path('dashboard/',views.DashBoard),
    path('Usuarios/', views.UsuariosWeb),
    path('Productos/',views.ProductosWeb),
    path('Reporte/',views.ReporteWeb),
    path('ListaV/',views.ListaWeb),


    path('crearUser/', views.CrearUsuario),
    path('eliminarUser/', views.eliminarUsers),
    path('modificaruser/',views.modificarUser),
    path('buscarU/',views.buscarU),
    

    path('crearProducto/',views.añadirProducto),
    path('eliminarProducto/', views.eliminarProducto),
    path('modificarProducto/',views.modificarProducto),
    path('buscarP/',views.buscarP),

    path('crearListaV/',views.crearLista),
    path('eliminarLV/',views.eliminarLista),
    path('buscarLV/',views.buscarlv),
    path('asignarLista/',views.asignarLista),

    path('PregLV/',views.PregLV),

    path('adicionarPLV/',views.adicionarPregunta),
    path('eliminarPregunta/', views.eliminarPreg),

]
