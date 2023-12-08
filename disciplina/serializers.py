from .models import Disciplina
from rest_framework import serializers


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [
            'nome',
            'codigo'
        ]
