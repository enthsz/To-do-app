# Generated by Django 5.0.5 on 2024-05-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_customuser_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(blank=True, max_length='500', null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]