from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    dataNascimento = models.DateField()
