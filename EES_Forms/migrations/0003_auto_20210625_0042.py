# Generated by Django 3.2.4 on 2021-06-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0002_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='date',
            field=models.CharField(default='false', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forms',
            name='submitted',
            field=models.CharField(default='water', max_length=30),
            preserve_default=False,
        ),
    ]
