# Generated by Django 3.1.5 on 2021-01-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0013_auto_20210121_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='myweek',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='myday',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
