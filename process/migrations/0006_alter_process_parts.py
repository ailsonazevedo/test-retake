# Generated by Django 4.1.2 on 2022-10-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_alter_process_judicialclass_delete_judicialclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='parts',
            field=models.ManyToManyField(related_name='parts', to='process.parts'),
        ),
    ]