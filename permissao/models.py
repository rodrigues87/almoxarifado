from django.db import models


class Permissao(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Permissão"
