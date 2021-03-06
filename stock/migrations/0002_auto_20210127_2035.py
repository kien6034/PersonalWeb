# Generated by Django 3.1.5 on 2021-01-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='buy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='is_owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stock',
            name='sell',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to='stock.stock')),
            ],
        ),
    ]
