# Generated by Django 3.1.5 on 2021-01-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0022_auto_20210122_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myweek',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
