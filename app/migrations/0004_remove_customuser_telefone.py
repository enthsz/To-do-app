# Generated by Django 5.0.5 on 2024-05-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customuser_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='telefone',
        ),
    ]
