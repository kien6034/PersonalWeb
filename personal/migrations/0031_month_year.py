# Generated by Django 3.1.5 on 2021-01-24 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0030_auto_20210124_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=0)),
                ('total_earn', models.IntegerField(default=0)),
                ('total_spend', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('name', models.IntegerField(default=0)),
                ('total_earn', models.IntegerField(default=0)),
                ('total_spend', models.IntegerField(default=0)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month', to='personal.year')),
            ],
        ),
    ]
