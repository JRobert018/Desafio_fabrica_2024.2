from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.ManyToManyField(Genero)
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return self.titulo
