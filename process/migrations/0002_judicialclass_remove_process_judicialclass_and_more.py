# Generated by Django 4.1.1 on 2022-10-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='judicialClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Judicial Class',
                'verbose_name_plural': 'Judicial Classes',
            },
        ),
        migrations.RemoveField(
            model_name='process',
            name='judicialClass',
        ),
        migrations.AddField(
            model_name='process',
            name='judicialClass',
            field=models.ManyToManyField(to='process.judicialclass', verbose_name='Judicial Class'),
        ),
    ]