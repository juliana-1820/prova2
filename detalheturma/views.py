from rest_framework import generics
from .models import DetalheTurma
from rest_framework import viewsets
from .serializers import DetalheTurmaSerializer

class DetalheTurmaView(viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer