# Generated by Django 3.1.5 on 2021-02-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20210213_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tfrom',
            field=models.CharField(blank=True, choices=[('ST', 'Stock'), ('SP', 'Spending'), ('EA', 'Earning'), ('CA', 'Cash'), ('CR', 'Crypto')], max_length=2, null=True),
        ),
    ]
