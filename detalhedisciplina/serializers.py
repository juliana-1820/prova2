from .models import DetalheDisciplina
from rest_framework import serializers


class DetalheDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheDisciplina
        fields = [
            'curso',
            'disciplina'
        ]
