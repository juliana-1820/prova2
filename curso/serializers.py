from .models import Curso
from rest_framework import serializers


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'nome',
            'codigo'
        ]
