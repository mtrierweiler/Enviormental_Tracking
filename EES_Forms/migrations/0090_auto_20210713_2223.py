# Generated by Django 3.2.4 on 2021-07-14 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0089_auto_20210713_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 22, 23, 11, 582979)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 22, 23, 11, 582996)),
        ),
        migrations.AlterField(
            model_name='user_profile_model',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
