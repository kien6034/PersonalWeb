# Generated by Django 3.1.5 on 2021-01-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0035_auto_20210127_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='myday',
            name='reward',
            field=models.IntegerField(default=0),
        ),
    ]
