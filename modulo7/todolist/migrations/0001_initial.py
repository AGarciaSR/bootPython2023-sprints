# Generated by Django 4.2.2 on 2023-06-30 10:59

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
                ('descripcion', models.TextField()),
                ('etiqueta', models.CharField(max_length=50, null=True)),
                ('prioridad', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('fecha_origen', models.DateField(default=datetime.date.today, editable=False)),
                ('fecha_limite', models.DateField(null=True)),
                ('completada', models.BooleanField()),
                ('fecha_completada', models.DateField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_limite', 'prioridad'],
            },
        ),
    ]
