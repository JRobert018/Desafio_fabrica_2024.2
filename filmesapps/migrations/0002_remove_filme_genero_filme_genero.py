# Generated by Django 5.1 on 2024-08-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmesapps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='genero',
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ManyToManyField(to='filmesapps.genero'),
        ),
    ]
