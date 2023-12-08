from django.db import models

class DetalheDisciplina(models.Model):
    curso = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
