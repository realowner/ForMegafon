# Generated by Django 4.0.5 on 2022-06-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleclibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.DateField(verbose_name='Дата издания'),
        ),
    ]
