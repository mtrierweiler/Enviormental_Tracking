# Generated by Django 3.2.4 on 2021-06-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0029_user_profile_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suba5_model',
            name='describe_background_stop',
        ),
        migrations.AddField(
            model_name='suba5_model',
            name='describe_emissions_point_start',
            field=models.CharField(default='n/a', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suba5_model',
            name='describe_emissions_point_stop',
            field=models.CharField(default='n/a', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_profile_model',
            name='cert_date',
            field=models.DateField(blank=True),
        ),
    ]
