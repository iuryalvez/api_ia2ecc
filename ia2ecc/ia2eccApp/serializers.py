from rest_framework import serializers
from .models import User, Animal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nome', 'whatsapp', 'data_cadastro', 'data_ultimo_acesso']

class AnimalSerializer(serializers.ModelSerializer):
    idade = serializers.ReadOnlyField()
    fase_vida = serializers.ReadOnlyField()

    class Meta:
        model = Animal
        fields = ['usuario', 'nome', 'especie', 'raca', 'data_nascimento', 'peso', 'condicao_corporal',
                  'gestacao', 'semana_gestacao', 'lactacao', 'semana_lactacao', 'foto', 'idade', 'fase_vida']
