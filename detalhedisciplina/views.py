from rest_framework import generics
from .models import DetalheDisciplina
from rest_framework import viewsets
from .serializers import DetalheDisciplinaSerializer

class DetalheDisciplinaView(viewsets.ModelViewSet):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer