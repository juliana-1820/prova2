from rest_framework import generics
from .models import Turma
from rest_framework import viewsets
from .serializers import TurmaSerializer

class TurmaView(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer