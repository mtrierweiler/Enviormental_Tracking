# Generated by Django 3.2.4 on 2021-08-02 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0154_auto_20210801_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formo_model',
            name='month',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 18, 18, 782626)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 11, 21, 18, 18, 782639)),
        ),
    ]
