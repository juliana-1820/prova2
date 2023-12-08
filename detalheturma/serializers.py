from .models import DetalheTurma
from rest_framework import serializers


class DetalheTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheTurma
        fields = [
            'aluno',
            'professor',
            'turma'
        ]
