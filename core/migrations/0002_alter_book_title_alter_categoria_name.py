# Generated by Django 5.0.7 on 2024-10-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
