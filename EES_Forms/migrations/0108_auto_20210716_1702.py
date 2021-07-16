# Generated by Django 3.2.4 on 2021-07-16 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0107_auto_20210716_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bat_info_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='daily_battery_profile_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forma2_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forma3_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forma4_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_0',
            field=models.CharField(blank=True, choices=[('foo', 'Foo Bar'), ('aackerman', 'Anthony Ackerman'), ('kjanis', 'Kerra Janis'), ('tlicht', 'Tristian Licht'), ('BigPenis', 'Micah Trierweiler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_1',
            field=models.CharField(blank=True, choices=[('foo', 'Foo Bar'), ('aackerman', 'Anthony Ackerman'), ('kjanis', 'Kerra Janis'), ('tlicht', 'Tristian Licht'), ('BigPenis', 'Micah Trierweiler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_2',
            field=models.CharField(blank=True, choices=[('foo', 'Foo Bar'), ('aackerman', 'Anthony Ackerman'), ('kjanis', 'Kerra Janis'), ('tlicht', 'Tristian Licht'), ('BigPenis', 'Micah Trierweiler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_3',
            field=models.CharField(blank=True, choices=[('foo', 'Foo Bar'), ('aackerman', 'Anthony Ackerman'), ('kjanis', 'Kerra Janis'), ('tlicht', 'Tristian Licht'), ('BigPenis', 'Micah Trierweiler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formb_model',
            name='observer_4',
            field=models.CharField(blank=True, choices=[('foo', 'Foo Bar'), ('aackerman', 'Anthony Ackerman'), ('kjanis', 'Kerra Janis'), ('tlicht', 'Tristian Licht'), ('BigPenis', 'Micah Trierweiler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formd_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forme_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf1_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf2_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf3_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf4_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf5_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf6_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formf7_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formg1_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formh_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formi_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forml_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formm_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='issues_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='add_days',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 17, 2, 10, 972186)),
        ),
        migrations.AlterField(
            model_name='pt_admin1_model',
            name='days_left',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 26, 17, 2, 10, 972200)),
        ),
        migrations.AlterField(
            model_name='suba1_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='suba5_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subc',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user_profile_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
