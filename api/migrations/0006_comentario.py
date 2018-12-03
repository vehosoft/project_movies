# Generated by Django 2.1.3 on 2018-12-02 23:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20181202_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('pelicula_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comentarios', to='api.Pelicula')),
                ('usuario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comentarios', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
