# Generated by Django 3.1.5 on 2021-02-28 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0039_auto_20210228_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='myday',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='day_quote', to='personal.quote'),
        ),
    ]