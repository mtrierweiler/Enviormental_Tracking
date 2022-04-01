# Generated by Django 3.2.7 on 2022-04-01 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0021_auto_20220331_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forma3_model',
            old_name='l_oven1',
            new_name='l_leak_json',
        ),
        migrations.RenameField(
            model_name='forma3_model',
            old_name='om_oven1',
            new_name='om_leak_json',
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 23, 25, 42, 736923)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 23, 25, 42, 736941)),
        ),
    ]
