# Generated by Django 4.1.6 on 2024-05-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumaguaAPP', '0005_remove_reporte_dato_extra_remove_reporte_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebederos',
            name='dato_extra',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='reporte',
            name='descripcion',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]