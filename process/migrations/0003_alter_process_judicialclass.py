# Generated by Django 4.1.1 on 2022-10-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_judicialclass_remove_process_judicialclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='judicialClass',
            field=models.ManyToManyField(to='process.judicialclass'),
        ),
    ]