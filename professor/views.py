from rest_framework import generics
from .models import Professor
from rest_framework import viewsets
from .serializers import ProfessorSerializer

class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer