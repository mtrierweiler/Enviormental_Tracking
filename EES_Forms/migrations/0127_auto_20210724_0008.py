# Generated by Django 3.2.5 on 2021-07-24 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0126_auto_20210723_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forma2_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma3_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='forma4_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_0',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_1',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_2',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_3',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_4',
            field=models.CharField(blank=True, choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forme_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 0, 8, 3, 391006)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 0, 8, 3, 391021)),
        ),
        migrations.AlterField(
            model_name='suba1_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
        migrations.AlterField(
            model_name='subc',
            name='observer',
            field=models.CharField(choices=[('Foo Bar', 'Foo Bar'), ('Anthony Ackerman', 'Anthony Ackerman'), ('Kerra Janis', 'Kerra Janis'), ('Tristian Licht', 'Tristian Licht'), ('Micah Trierweiler', 'Micah Trierweiler'), ('Tobias Ackerman', 'Tobias Ackerman')], max_length=30),
        ),
    ]
