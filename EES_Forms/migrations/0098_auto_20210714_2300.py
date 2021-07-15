# Generated by Django 3.2.4 on 2021-07-15 03:00

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0097_auto_20210714_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='formb_model',
            name='additional_surpressant_1',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='additional_surpressant_2',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='additional_surpressant_3',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='additional_surpressant_4',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='barrier_thickness_1',
            field=models.CharField(choices=[('none', 'None'), ('0" - 1/4"', '0" - 1/4"'), ('1/4" - 1/2"', '1/4" - 1/2"'), ('1/2" - 3/4"', '1/2" - 3/4"'), ('3/4" - 1"', '3/4" - 1"'), ('1" - 2"', '1" - 2"')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='barrier_thickness_2',
            field=models.CharField(choices=[('none', 'None'), ('0" - 1/4"', '0" - 1/4"'), ('1/4" - 1/2"', '1/4" - 1/2"'), ('1/2" - 3/4"', '1/2" - 3/4"'), ('3/4" - 1"', '3/4" - 1"'), ('1" - 2"', '1" - 2"')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='barrier_thickness_3',
            field=models.CharField(choices=[('none', 'None'), ('0" - 1/4"', '0" - 1/4"'), ('1/4" - 1/2"', '1/4" - 1/2"'), ('1/2" - 3/4"', '1/2" - 3/4"'), ('3/4" - 1"', '3/4" - 1"'), ('1" - 2"', '1" - 2"')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='barrier_thickness_4',
            field=models.CharField(choices=[('none', 'None'), ('0" - 1/4"', '0" - 1/4"'), ('1/4" - 1/2"', '1/4" - 1/2"'), ('1/2" - 3/4"', '1/2" - 3/4"'), ('3/4" - 1"', '3/4" - 1"'), ('1" - 2"', '1" - 2"')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='breeze_1',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='breeze_2',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='breeze_3',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='breeze_4',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='coal_vessel_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='coal_vessel_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='coal_vessel_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='coal_vessel_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='comments_1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='formb_model',
            name='comments_2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='formb_model',
            name='comments_3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='formb_model',
            name='comments_4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='formb_model',
            name='fugitive_dust_observed_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='fugitive_dust_observed_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='fugitive_dust_observed_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='fugitive_dust_observed_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='loader_lowered_1',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='loader_lowered_2',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='loader_lowered_3',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='loader_lowered_4',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='observer_1',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='observer_2',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='observer_3',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='observer_4',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='pushed_back_1',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='pushed_back_2',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='pushed_back_3',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='pushed_back_4',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='spills_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='spills_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='spills_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='spills_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_active_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_active_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_active_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_active_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_applied_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_applied_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_applied_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='supressant_applied_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surface_quality_1',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surface_quality_2',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surface_quality_3',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surface_quality_4',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surpressant_crust_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surpressant_crust_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surpressant_crust_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='surpressant_crust_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='time_1',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='time_2',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='time_3',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='time_4',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='water_sprays_1',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='water_sprays_2',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='water_sprays_3',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='water_sprays_4',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='weather_1',
            field=models.CharField(choices=[('clear', 'Clear'), ('cloudy', 'Cloudy'), ('rain', 'Rain'), ('snow', 'Snow'), ('excessive wind', 'Excessive Wind')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='weather_2',
            field=models.CharField(choices=[('clear', 'Clear'), ('cloudy', 'Cloudy'), ('rain', 'Rain'), ('snow', 'Snow'), ('excessive wind', 'Excessive Wind')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='weather_3',
            field=models.CharField(choices=[('clear', 'Clear'), ('cloudy', 'Cloudy'), ('rain', 'Rain'), ('snow', 'Snow'), ('excessive wind', 'Excessive Wind')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='weather_4',
            field=models.CharField(choices=[('clear', 'Clear'), ('cloudy', 'Cloudy'), ('rain', 'Rain'), ('snow', 'Snow'), ('excessive wind', 'Excessive Wind')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wharf_1',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wharf_2',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wharf_3',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wharf_4',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wind_speed_1',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wind_speed_2',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wind_speed_3',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='wind_speed_4',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_face_exceed_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_face_exceed_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_face_exceed_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_face_exceed_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_water_sprays_1',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_water_sprays_2',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_water_sprays_3',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formb_model',
            name='working_water_sprays_4',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 22, 58, 1, 727250)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 22, 58, 1, 727265)),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='cert_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='direction_from',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='estab',
            field=models.CharField(max_length=5),
        ),
    ]
