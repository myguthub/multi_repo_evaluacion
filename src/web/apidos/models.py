from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    grupo=models.CharField(max_length=50)
    anno=models.PositiveIntegerField()