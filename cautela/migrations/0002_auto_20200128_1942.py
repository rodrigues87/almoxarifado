# Generated by Django 2.2.7 on 2020-01-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cautela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cautela',
            name='data_de_devolucao',
            field=models.DateField(),
        ),
    ]
