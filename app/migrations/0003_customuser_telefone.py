# Generated by Django 5.0.5 on 2024-05-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tarefa'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telefone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]