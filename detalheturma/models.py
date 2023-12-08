from django.db import models

class DetalheTurma (models.Model):
    aluno = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)