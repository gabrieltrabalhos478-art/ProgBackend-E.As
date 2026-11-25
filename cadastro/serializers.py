from rest_framework import serializers
from .models import Usuario


# Serializer que converte objetos Usuario para JSON e vice-versa
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email']
