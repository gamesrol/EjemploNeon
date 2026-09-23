from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField(verbose_name="Año de publicación")
    categorias = models.ManyToManyField(Categoria)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - ({self.autor})"

