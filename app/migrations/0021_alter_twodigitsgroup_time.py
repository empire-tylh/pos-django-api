# Generated by Django 3.2.9 on 2022-11-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_twodigitsgroup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twodigitsgroup',
            name='time',
            field=models.CharField(default='m', max_length=10),
        ),
    ]
