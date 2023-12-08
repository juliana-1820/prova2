from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)