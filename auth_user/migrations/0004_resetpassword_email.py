# Generated by Django 3.1.4 on 2021-02-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_resetpassword_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetpassword',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
