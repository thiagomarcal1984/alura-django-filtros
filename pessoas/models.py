from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome
        