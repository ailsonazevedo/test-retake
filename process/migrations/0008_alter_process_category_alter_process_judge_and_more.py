# Generated by Django 4.1.2 on 2022-10-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0007_alter_process_category_alter_process_judge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='category',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Categoria:'),
        ),
        migrations.AlterField(
            model_name='process',
            name='judge',
            field=models.CharField(max_length=500, verbose_name='Juiz:'),
        ),
        migrations.AlterField(
            model_name='process',
            name='judicialClass',
            field=models.CharField(max_length=1000, verbose_name='Classe:'),
        ),
        migrations.AlterField(
            model_name='process',
            name='number',
            field=models.CharField(max_length=1000, verbose_name='Número do Processo'),
        ),
        migrations.AlterField(
            model_name='process',
            name='parts',
            field=models.ManyToManyField(related_name='parts', to='process.parts', verbose_name='Partes'),
        ),
        migrations.AlterField(
            model_name='process',
            name='topic',
            field=models.CharField(max_length=1000, verbose_name='Assunto:'),
        ),
    ]
