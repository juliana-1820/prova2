from rest_framework import generics
from .models import Curso
from rest_framework import viewsets
from .serializers import CursoSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer