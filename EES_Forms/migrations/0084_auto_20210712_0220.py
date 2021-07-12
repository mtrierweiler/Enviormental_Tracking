# Generated by Django 3.2.4 on 2021-07-12 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0083_auto_20210712_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='formF2_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observer', models.CharField(max_length=30)),
                ('time', models.TimeField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('retain_date', models.DateField(blank=True)),
                ('status_1', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_2', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_3', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_4', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_5', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_6', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('status_7', models.CharField(choices=[('N/A', 'N/A'), ('OK', 'OK'), ('Not OK', 'Not OK')], max_length=30)),
                ('comments_1', models.CharField(max_length=30)),
                ('comments_2', models.CharField(max_length=30)),
                ('comments_3', models.CharField(max_length=30)),
                ('comments_4', models.CharField(max_length=30)),
                ('comments_5', models.CharField(max_length=30)),
                ('comments_6', models.CharField(max_length=30)),
                ('comments_7', models.CharField(max_length=30)),
                ('action_1', models.CharField(max_length=30)),
                ('action_2', models.CharField(max_length=30)),
                ('action_3', models.CharField(max_length=30)),
                ('action_4', models.CharField(max_length=30)),
                ('action_5', models.CharField(max_length=30)),
                ('action_6', models.CharField(max_length=30)),
                ('action_7', models.CharField(max_length=30)),
                ('waste_des_1', models.CharField(max_length=30)),
                ('waste_des_2', models.CharField(max_length=30)),
                ('waste_des_3', models.CharField(max_length=30)),
                ('waste_des_4', models.CharField(max_length=30)),
                ('containers_1', models.IntegerField()),
                ('containers_2', models.IntegerField(blank=True, null=True)),
                ('containers_3', models.IntegerField(blank=True, null=True)),
                ('containers_4', models.IntegerField(blank=True, null=True)),
                ('waste_codes_1', models.CharField(choices=[('universal', 'UNIV'), ('non-hazardous ', 'NON-HAZ'), ('hazardous', 'HAZ')], max_length=30)),
                ('waste_codes_2', models.CharField(blank=True, choices=[('universal', 'UNIV'), ('non-hazardous ', 'NON-HAZ'), ('hazardous', 'HAZ')], max_length=30, null=True)),
                ('waste_codes_3', models.CharField(blank=True, choices=[('universal', 'UNIV'), ('non-hazardous ', 'NON-HAZ'), ('hazardous', 'HAZ')], max_length=30, null=True)),
                ('waste_codes_4', models.CharField(blank=True, choices=[('universal', 'UNIV'), ('non-hazardous ', 'NON-HAZ'), ('hazardous', 'HAZ')], max_length=30, null=True)),
                ('dates_1', models.DateField(blank=True)),
                ('dates_2', models.DateField(blank=True, null=True)),
                ('dates_3', models.DateField(blank=True, null=True)),
                ('dates_4', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='forms',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 2, 20, 6, 662625)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 2, 20, 6, 662639)),
        ),
    ]
