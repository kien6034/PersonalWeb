# Generated by Django 3.1.5 on 2021-02-02 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_transaction_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='method',
        ),
    ]
