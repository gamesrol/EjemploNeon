"""
URL configuration for biblioteca_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from catalogo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/registro/', views.vista_registro, name='registro'),
    path('autores/', views.vista_lista_autores, name='autores'),
    path('categorias/', views.vista_lista_categorias, name='categorias'),
    path('autor/nuevo/', views.vista_crear_autor, name='crear_autor'),
    path('autor/<int:id_autor>/editar/', views.vista_editar_autor, name='editar_autor'),
    path('autor/<int:id_autor>/borrar/', views.vista_borrar_autor, name='borrar_autor'),
    path('categoria/nuevo/', views.vista_crear_categoria, name='crear_categoria'),
    path('categoria/<int:id_categoria>/editar/', views.vista_editar_categoria, name='editar_categoria'),
    path('categoria/<int:id_categoria>/borrar/', views.vista_borrar_categoria, name='borrar_categoria'),
    path('catalogo/', views.vista_catalogo, name='catalogo'),
    path('libro/<int:id_libro>/', views.vista_detalle, name='detalle'),
    path('libro/nuevo/', views.vista_crear_libro, name='crear'),
    path('libro/<int:id_libro>/editar/', views.vista_editar_libro, name='editar'),
    path('libro/<int:id_libro>/borrar/', views.vista_borrar_libro, name='borrar'),
]
