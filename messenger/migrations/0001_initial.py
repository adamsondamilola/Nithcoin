# Generated by Django 3.1.4 on 2021-01-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('receiver_id', models.IntegerField(blank=True, null=True)),
                ('sender_id', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='messages/')),
                ('seen', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
