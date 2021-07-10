# Generated by Django 3.1.3 on 2021-07-08 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0051_auto_20210708_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily_battery_profile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreman', models.CharField(choices=[('Zajas', 'Zajas'), ('Folding', 'Folding'), ('Cooper', 'Cooper'), ('Lopez', 'Lopez')], max_length=10)),
                ('crew', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('inop_ovens', models.CharField(max_length=2)),
                ('date_save', models.DateField(auto_now_add=True)),
                ('time_log', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 6, 14, 49, 11, 422515)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 14, 49, 11, 422535)),
        ),
    ]
