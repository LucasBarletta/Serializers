# Generated by Django 2.2.5 on 2019-09-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='idade',
            field=models.CharField(max_length=255, verbose_name='Idade'),
        ),
    ]
