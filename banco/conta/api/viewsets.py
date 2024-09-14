from urllib import response
from rest_framework import viewsets
from conta.api import serializers
from conta import models


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContaSerializer
    queryset = models.Conta.objects.all()


class RegistroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistroBancarioSerializer
    queryset = models.RegistroBancario.objects.all()
