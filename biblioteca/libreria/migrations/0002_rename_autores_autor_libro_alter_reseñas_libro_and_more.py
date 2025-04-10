# Generated by Django 5.2 on 2025-04-10 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autores',
            new_name='Autor',
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('resumen', models.TextField()),
                ('autores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.autor')),
            ],
        ),
        migrations.AlterField(
            model_name='reseñas',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.libro'),
        ),
        migrations.DeleteModel(
            name='Libros',
        ),
    ]
