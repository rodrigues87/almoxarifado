from django.contrib import admin

# Register your models here.
from cautela.models import Cautela


class CautelaAdmin(admin.ModelAdmin):
    exclude = ('autor','data_de_cautela',)

admin.site.register(Cautela,CautelaAdmin)