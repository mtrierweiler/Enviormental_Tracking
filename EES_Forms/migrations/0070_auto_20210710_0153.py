# Generated by Django 3.2.4 on 2021-07-10 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0069_auto_20210710_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 8, 1, 53, 31, 21903)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 20, 1, 53, 31, 21917)),
        ),
    ]
