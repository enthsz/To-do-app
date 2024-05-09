# Generated by Django 5.0.5 on 2024-05-07 17:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tarefa_descricao_alter_tarefa_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]