from django.db import models

# Create your models here.
class userlogs(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    device = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.country

class ResetPassword(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    status = models.IntegerField(blank=True, null=True)
    temp_password = models.CharField(blank=True, null=True, max_length=255)
    code = models.CharField(blank=True, null=True, max_length=255)
    unique = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()
