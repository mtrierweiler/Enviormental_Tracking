# Generated by Django 3.2.4 on 2021-07-17 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0114_auto_20210716_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead1',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead10',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead11',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead12',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead2',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead3',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead4',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead5',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead6',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead7',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead8',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='ARead9',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead1',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead10',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead11',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead12',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead2',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead3',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead4',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead5',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead6',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead7',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead8',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='TRead9',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 20, 15, 12, 987640)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 26, 20, 15, 12, 987654)),
        ),
    ]
