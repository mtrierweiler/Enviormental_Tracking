# Generated by Django 3.2.4 on 2021-07-16 23:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0108_auto_20210716_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='formcreadings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formcreadings',
            name='form',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='EES_Forms.subc'),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 19, 1, 32, 962158)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 26, 19, 1, 32, 962172)),
        ),
    ]
