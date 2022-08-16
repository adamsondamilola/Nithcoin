# Generated by Django 3.1.4 on 2021-01-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='full_face',
            field=models.ImageField(blank=True, null=True, upload_to='vendors/'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='id_card',
            field=models.ImageField(blank=True, null=True, upload_to='vendors/'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='minimum',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendors',
            name='proof_of_residence',
            field=models.ImageField(blank=True, null=True, upload_to='vendors/'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='selling_at',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
