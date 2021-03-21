# Generated by Django 3.1.5 on 2021-01-21 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_myday_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='daytask',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='daytask',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.CreateModel(
            name='WeekTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
                ('weight', models.IntegerField(default=0)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekTask', to='personal.myweek')),
            ],
        ),
    ]
