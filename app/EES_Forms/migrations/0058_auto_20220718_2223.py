# Generated by Django 3.2.7 on 2022-07-19 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0057_auto_20220718_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sop_model',
            name='pdf_link',
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 22, 23, 0, 172189)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 22, 23, 0, 172207)),
        ),
    ]
