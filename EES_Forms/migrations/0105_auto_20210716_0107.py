# Generated by Django 3.2.4 on 2021-07-16 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0104_auto_20210715_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='frequency',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quaterly', 'Quaterly '), ('Semi-Annual', 'Semi-Annual'), ('Annual', 'Annual')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 1, 7, 46, 620267)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 26, 1, 7, 46, 620281)),
        ),
    ]
