from django.contrib import admin
from .models import Libro, Autor, Categoria

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Categoria)