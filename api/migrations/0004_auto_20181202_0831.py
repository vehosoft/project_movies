# Generated by Django 2.1.3 on 2018-12-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181202_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.CharField(max_length=20, verbose_name='Fecha de estreno'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(verbose_name='Sinopsis'),
        ),
    ]
