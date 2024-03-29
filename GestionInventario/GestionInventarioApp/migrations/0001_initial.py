# Generated by Django 4.1.4 on 2023-03-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('codigo_costo', models.CharField(choices=[('1', 'Muy Barato'), ('2', 'Barato'), ('3', 'Intermedio'), ('4', 'Alto'), ('5', 'Muy Alto')], max_length=25)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(to='GestionInventarioApp.categoria')),
            ],
        ),
    ]
