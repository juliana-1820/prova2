from rest_framework import generics
from .models import DetalheCurso
from rest_framework import viewsets
from .serializers import DetalheCursoSerializer

class DetalheCursoView(viewsets.ModelViewSet):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer