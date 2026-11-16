from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)  # int PK
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    anio_nacimiento = models.IntegerField()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key=True)  # int PK
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.IntegerField()
    # Un autor escribe 0..N libros; cada libro tiene exactamente 1 autor (columna autor_id)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")

    def __str__(self):
        return self.titulo
