# Generated by Django 4.2.2 on 2023-07-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_prioridad_alter_tarea_user_id_alter_tarea_prioridad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prioridad',
            name='id',
        ),
        migrations.AlterField(
            model_name='prioridad',
            name='priority',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]