# Generated by Django 3.1.5 on 2021-01-27 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0034_delete_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Figure',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]