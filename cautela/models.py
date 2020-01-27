from django.db import models

from cadastro.models import Cadastro
from material.models import Material
from permissao.models import Permissao


class Cautela(models.Model):
    requerente = models.ForeignKey(Cadastro, on_delete=models.CASCADE,related_name='requerente')
    autor = models.ForeignKey(Cadastro, on_delete=models.CASCADE,related_name='autor')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    data_de_cautela = models.DateTimeField(auto_now=True)
    data_de_devolucao = models.DateTimeField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.material

    class Meta:
        verbose_name_plural = "Cautela"
