from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import AdminDateWidget

from cautela.models import Cautela
from django.db import models
from datetime import datetime


def devolver_material(modeladmin, request, queryset):
    for cautela in queryset:
        cautela.data_de_devolucao = datetime.now()
        cautela.save()


devolver_material.short_description = 'Devolver Material'


class CautelaAdmin(admin.ModelAdmin):
    exclude = ('autor', 'data_de_cautela', 'data_de_devolucao')
    list_display = ('material', 'requerente', 'data_de_cautela', 'data_de_devolucao', 'quantidade_emprestada')
    actions = [devolver_material, ]

    formfield_overrides = {
        models.DateField: {'widget': AdminDateWidget},
    }

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.autor:
            instance.autor = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Cautela, CautelaAdmin)
