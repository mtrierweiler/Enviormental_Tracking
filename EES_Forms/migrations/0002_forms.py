# Generated by Django 3.2.4 on 2021-06-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EES_Forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=30)),
            ],
        ),
    ]
