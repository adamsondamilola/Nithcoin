# Generated by Django 3.1.4 on 2021-01-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_currentprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentprice',
            name='ntc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='currentprice',
            name='usd',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
