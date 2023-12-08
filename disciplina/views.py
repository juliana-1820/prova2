from rest_framework import generics
from .models import Disciplina
from rest_framework import viewsets
from .serializers import DisciplinaSerializer

class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer