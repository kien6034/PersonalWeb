# Generated by Django 3.1.5 on 2021-01-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_auto_20210122_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myday',
            name='quote',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
