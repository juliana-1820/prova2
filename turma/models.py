from django.db import models

class Turma(models.Model):
    codigoturma = models.CharField(max_length=100)
    codigocurso = models.CharField(max_length=100)
