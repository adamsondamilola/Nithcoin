from django.db import models

# Create your models here.
class proofs(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    transaction_id = models.CharField(blank=True, null=True, max_length=255)
    pop = models.ImageField(blank=True, null=True, upload_to="proofs/")
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id

class wallets(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=255)
    balance = models.FloatField(blank=True, null=True)
    sent = models.FloatField(blank=True, null=True)
    received = models.FloatField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pin = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id

class AccountNums(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=255)
    number = models.CharField(unique=True, max_length=255)
    label = models.CharField(blank=True, null=True, max_length=255)
    balance = models.FloatField(blank=True, null=True)
    sent = models.FloatField(blank=True, null=True)
    received = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id
