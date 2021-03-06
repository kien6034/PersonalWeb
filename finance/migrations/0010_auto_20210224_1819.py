# Generated by Django 3.1.5 on 2021-02-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20210217_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tfrom',
            field=models.CharField(blank=True, choices=[('Stock', 'Stock'), ('Spending', 'Spending'), ('Earning', 'Earning'), ('Cash', 'Cash'), ('Crypto', 'Crypto'), ('Avail', 'Avail')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tto',
            field=models.CharField(blank=True, choices=[('Stock', 'Stock'), ('Spending', 'Spending'), ('Earning', 'Earning'), ('Cash', 'Cash'), ('Crypto', 'Crypto'), ('Avail', 'Avail')], max_length=8, null=True),
        ),
    ]
