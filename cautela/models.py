from django.contrib.auth.models import User
from django.db import models

from cadastro.models import Cadastro
from material.models import Material
from permissao.models import Permissao


class Cautela(models.Model):
    requerente = models.ForeignKey(Cadastro, on_delete=models.CASCADE,related_name='requerente')
    autor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='autor')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    data_de_cautela = models.DateTimeField(auto_now=True)
    data_de_devolucao = models.DateField(blank=True,null=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.material.nome

    class Meta:
        verbose_name_plural = "Cautela"
