# Generated by Django 3.1.4 on 2021-01-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20210112_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('method', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
