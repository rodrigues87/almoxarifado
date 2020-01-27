# Generated by Django 2.2.7 on 2020-01-27 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalQdi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(blank=True, max_length=10, null=True)),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Local Qdi',
            },
        ),
        migrations.CreateModel(
            name='LocalQo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(blank=True, max_length=10, null=True)),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Local Qo',
            },
        ),
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localAdido', models.CharField(blank=True, max_length=150, null=True)),
                ('localQdi', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locais.LocalQdi')),
                ('localQo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locais.LocalQo')),
            ],
            options={
                'verbose_name_plural': 'Locais',
            },
        ),
    ]
