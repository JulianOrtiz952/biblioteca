from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    resumen = models.TextField()

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.libro.titulo} - {self.calificacion}'
    
    
