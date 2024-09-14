from rest_framework import serializers
from conta import models


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = "__all__"


class ContaSerializer(serializers.ModelSerializer):
    
    def validate_cliente(self, value):
        # Verifica se o cliente já tem uma conta bancária
        if models.Conta.objects.filter(cliente=value).exists():
            raise serializers.ValidationError("O cliente já possui uma conta bancária.")
        return value
    
    def create(self, validated_data):
        # Se passar na validação, cria a conta bancária
        return models.Conta.objects.create(**validated_data)
    
    class Meta:
        model = models.Conta
        fields = "__all__"


class RegistroBancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RegistroBancario
        fields = "__all__"