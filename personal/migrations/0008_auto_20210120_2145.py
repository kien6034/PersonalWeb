# Generated by Django 3.1.5 on 2021-01-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_myday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myday',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
