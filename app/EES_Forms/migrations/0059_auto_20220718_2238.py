# Generated by Django 3.2.7 on 2022-07-19 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0058_auto_20220718_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='sop_model',
            name='pdf_link',
            field=models.CharField(default='sop.pdf', max_length=90),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 22, 38, 38, 269577)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 28, 22, 38, 38, 269598)),
        ),
    ]
