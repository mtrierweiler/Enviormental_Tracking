# Generated by Django 3.2.7 on 2022-05-22 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0040_auto_20220520_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forme_model',
            name='comments1',
        ),
        migrations.RemoveField(
            model_name='forme_model',
            name='oven1',
        ),
        migrations.RemoveField(
            model_name='forme_model',
            name='source1',
        ),
        migrations.RemoveField(
            model_name='forme_model',
            name='time1',
        ),
        migrations.AddField(
            model_name='forme_model',
            name='goose_neck_data',
            field=models.CharField(default='{}', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 18, 38, 56, 375695)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 18, 38, 56, 375711)),
        ),
    ]
