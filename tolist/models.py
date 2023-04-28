from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Prioridades(models.Model):

    descripcion = models.CharField(max_length=15, blank=False, null=False)
    
    class Meta:
        verbose_name = "Prioridad"
        verbose_name_plural = "Prioridades"
    
    def _str_(self):
        return '{}-{}'.format(self.descripcion)


class Categorias(models.Model):

    descripcion = models.CharField(max_length=25, blank=False, null=False)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def _str_(self):
        return '{}-{}'.format(self.descripcion)
    

class Tareas(models.Model):

    descripcion = models.CharField(max_length=200, blank = False, null = False)
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column="id_user")
    id_prioridad = models.ForeignKey(Prioridades, models.DO_NOTHING, db_column='id_prioridad')
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
    estado = models.IntegerField(default = 1, blank = False, null = False)
    fecha_limite = models.DateTimeField(blank = True, null = True)
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
    
    def _str_(self):
        return '{}-{}'.format(self.descripcion)