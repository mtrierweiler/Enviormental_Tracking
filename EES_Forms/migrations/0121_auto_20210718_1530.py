# Generated by Django 3.2.4 on 2021-07-18 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0120_auto_20210716_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='suba5_model',
            name='notes',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forme_model',
            name='observer',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 15, 29, 57, 178212)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 15, 29, 57, 178227)),
        ),
    ]
