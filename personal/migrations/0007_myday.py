# Generated by Django 3.1.5 on 2021-01-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20210120_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
