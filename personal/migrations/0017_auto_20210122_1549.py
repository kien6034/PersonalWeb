# Generated by Django 3.1.5 on 2021-01-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20210122_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='myday',
            name='total_finished_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myday',
            name='total_weight',
            field=models.IntegerField(default=0),
        ),
    ]
