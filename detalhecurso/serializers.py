from .models import DetalheCurso
from rest_framework import serializers


class DetalheCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheCurso
        fields = [
            'curso',
            'turma'
        ]
