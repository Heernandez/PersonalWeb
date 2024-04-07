from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url = models.URLField(verbose_name="Url del repo",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #auto_now_add=True captura el valor y lo guarda, solo en la creacion
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización") # captura el valor y lo guarda en cada actualizacion

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
