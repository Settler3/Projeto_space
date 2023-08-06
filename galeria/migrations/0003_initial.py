# Generated by Django 4.2.3 on 2023-07-19 09:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galeria', '0002_delete_fotografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('publicada', models.BooleanField(default=False)),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.categoria')),
            ],
        ),
    ]
