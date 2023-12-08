from rest_framework import generics
from .models import Aluno
from rest_framework import viewsets
from .serializers import AlunoSerializer

class AlunoView(viewsets.ModelViewSet):
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer