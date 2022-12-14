# Generated by Django 3.2.9 on 2022-10-02 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_pricingrequest_rq_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_plan',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pricingrequest',
            name='rq_price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rq_price', to='app.pricing'),
        ),
        migrations.AlterField(
            model_name='pricingrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
