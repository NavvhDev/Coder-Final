from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombres', max_length = 200, blank= False, null= False)
    apellidos = models.CharField('Apellidos', max_length= 220, blank= False, null= False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 100, blank = False, null= False)
    estado = models.BooleanField('Estado', default = True)
    descripcion = models.TextField('Descripcion',max_length= 200, blank = False, null=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank= False, null= False)
    fecha_publicacion = models.DateField('Fecha de publicacion', blank= False, null= False)
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = "Libros"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo