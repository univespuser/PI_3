from django.db import models

# Create your models here.
class Post(models.Model):
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=14)
    servico = models.TextField()
