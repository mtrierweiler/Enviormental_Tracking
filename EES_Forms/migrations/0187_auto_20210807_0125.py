# Generated by Django 3.2.4 on 2021-08-07 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0186_auto_20210806_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 1, 25, 29, 562372)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 1, 25, 29, 562386)),
        ),
    ]
