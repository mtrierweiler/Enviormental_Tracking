# Generated by Django 3.2.4 on 2021-06-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0009_alter_subc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subc',
            name='truck_start_time',
            field=models.TimeField(max_length=30),
        ),
    ]
