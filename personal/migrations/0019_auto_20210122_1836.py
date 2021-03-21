# Generated by Django 3.1.5 on 2021-01-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0018_auto_20210122_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='myday',
            name='quote',
            field=models.CharField(default=None, max_length=256),
        ),
    ]