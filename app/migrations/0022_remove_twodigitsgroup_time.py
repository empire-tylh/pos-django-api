# Generated by Django 3.2.9 on 2022-11-17 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_twodigitsgroup_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twodigitsgroup',
            name='time',
        ),
    ]
