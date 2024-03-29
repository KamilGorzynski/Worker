# Generated by Django 2.2.5 on 2019-10-01 19:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20191001_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requesthistory',
            name='created_a',
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 1, 19, 1, 45, 987960, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='url_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.UrlObject'),
        ),
    ]
