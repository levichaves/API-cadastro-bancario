from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        ('corrente', 'Corrente'),
        ('poupanca', 'Poupança'),
    ]
    
    numero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50, choices=TIPO_CONTA_CHOICES)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas')

    def __str__(self):
        return f'Conta {self.numero} - {self.cliente.nome}'


class RegistroBancario(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='registros')

    def __str__(self):
        return f'{self.descricao} - {self.valor}'
