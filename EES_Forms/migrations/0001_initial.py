# Generated by Django 3.2.4 on 2021-06-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushTravels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observer', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('oven1', models.CharField(max_length=30)),
                ('oven2', models.CharField(max_length=30)),
                ('oven3', models.CharField(max_length=30)),
                ('oven4', models.CharField(max_length=30)),
            ],
        ),
    ]
