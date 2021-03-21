# Generated by Django 3.1.5 on 2021-01-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0026_taskgroup_sort_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='reward',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='taskgroup',
            name='reward_weight',
            field=models.IntegerField(default=0),
        ),
    ]