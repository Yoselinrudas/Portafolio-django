from django.db import models

# Create your models here.

class Portafoleos(models.Model):
    imagenes = models.CharField(max_length=200, blank=False)
    titulos = models.CharField(max_length=100, blank=False)
    descripciones = models.CharField(max_length=250, blank=False)
    tag = models.CharField(max_length=100, blank=False)
    url_github = models.CharField(max_length=200, blank=False)

    def save(self, *args, **kwargs):
        return super(Portafoleos, self).save(*args, **kwargs)
