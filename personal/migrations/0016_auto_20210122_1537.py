# Generated by Django 3.1.5 on 2021-01-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20210122_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myday',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]