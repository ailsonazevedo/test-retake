# Generated by Django 4.1.2 on 2022-10-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0010_alter_process_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='number',
            field=models.CharField(max_length=1000, unique=True, verbose_name='Número do Processo:'),
        ),
    ]
