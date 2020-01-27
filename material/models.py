from django.db import models


class Material(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Material"