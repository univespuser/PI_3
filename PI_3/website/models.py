from django.db import models

class categorias(models.TextChoices):
    M1 = 'M1', 'Mecanica - Motor/Cambio'
    M2 = 'M2', 'Mecanica - Outros'
    E1 = 'E1', 'Eletrica - Injecao Eletronica'
    E2 = 'E2', 'Eletrica - Outros'

# Create your models here.

class Solicitacao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=11)
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField()

class Post(models.Model):
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=14)
    servico = models.TextField()
    tipo = models.CharField(
            max_length=2,
            choices=categorias.choices,
            default=categorias.E1,
            )
    aprovado = models.BooleanField(default=False)

    #def get_tipo_label(self):
        #return self.tipo.get_tipo_display()

