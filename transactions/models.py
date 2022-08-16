from django.db import models

# Create your models here.
class transactions(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    amount = models.FloatField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=255)
    transaction_id = models.CharField(blank=True, null=True, max_length=255)
    sender = models.CharField(blank=True, null=True, max_length=255)
    receiver = models.CharField(blank=True, null=True, max_length=255)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id
