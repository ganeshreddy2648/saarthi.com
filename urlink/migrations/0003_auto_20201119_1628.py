# Generated by Django 3.1.3 on 2020-11-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlink', '0002_auto_20201119_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmod',
            name='basicurl',
            field=models.URLField(unique=True),
        ),
    ]
