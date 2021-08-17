# Generated by Django 3.2.4 on 2021-08-05 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0182_auto_20210804_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma1_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma2_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma3_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma4_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma5_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_10_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_11_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_12_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_13_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_14_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_15_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_16_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_1_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_2_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_3_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_4_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_5_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_6_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_7_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_8_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='forma5_readings_model',
            name='o1_9_reads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_0',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_1',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_2',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_3',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_4',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formc_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='observer1',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='observer2',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='observer3',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='observer4',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='observer5',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forme_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='obser_0',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='obser_1',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='obser_2',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='obser_3',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='obser_4',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_0',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_1',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_2',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_3',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_4',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_5',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='obser_6',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formm_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='formo_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='formp_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman'), ('Alyssa Kersanty', 'Alyssa Kersanty'), ('Roger Kalinowsky', 'Roger Kalinowsky'), ('Elise Ciak', 'Elise Ciak')], max_length=30),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 32, 1, 68910)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 15, 19, 32, 1, 68923)),
        ),
    ]
