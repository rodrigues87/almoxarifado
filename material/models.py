from django.db import models


class Material(models.Model):
    nome = models.CharField(max_length=150)
    quantidade_disponivel = models.IntegerField()
    consumo = models.BooleanField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Materiais"
