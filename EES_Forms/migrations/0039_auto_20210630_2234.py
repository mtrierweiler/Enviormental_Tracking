# Generated by Django 3.2.4 on 2021-06-30 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0038_auto_20210630_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suba5_readings_model',
            name='form',
        ),
        migrations.AddField(
            model_name='suba5_readings_model',
            name='penis',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='EES_Forms.suba5_model'),
            preserve_default=False,
        ),
    ]
