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

class Reseñas(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self):
        return f'{self.usuario} - {self.libro.titulo}'
    
    
    
    
    
    
    
    
    
    # class Meta:
    #     verbose_name_plural = 'Reseñas'
    #     ordering = ['-puntaje']
    #     index_together = [['libro', 'usuario']]
    #     unique_together = [['libro', 'usuario']]
    #     constraints = [
    #         models.CheckConstraint(check=models.Q(puntaje__gte=1, puntaje__lte=5), name='puntaje_valido'),
    #     ]
    #     permissions = [
    #         ('can_review_books', 'Puede revisar libros'),
    #         ('can_rate_books', 'Puede calificar libros'),
    #     ]
    #     indexes = [
    #         models.Index(fields=['libro', 'usuario']),
    #         models.Index(fields=['comentario'], name='comentario_idx'),
    #     ]
        