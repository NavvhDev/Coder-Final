# Generated by Django 5.0 on 2024-01-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_alter_autor_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.TextField(max_length=200, verbose_name='Descripcion'),
        ),
    ]