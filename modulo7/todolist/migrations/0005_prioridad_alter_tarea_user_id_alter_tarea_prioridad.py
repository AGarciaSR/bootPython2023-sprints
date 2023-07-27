# Generated by Django 4.2.2 on 2023-07-27 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0004_tarea_observacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prioridad', to='todolist.prioridad'),
        ),
    ]
