from django.db import models

# Create your models here.
class siteSettings(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    address = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=255)
    altphone = models.CharField(blank=True, null=True, max_length=255)
    sub_title = models.CharField(max_length=254, default=None, blank=True, null=True)
    symbol = models.CharField(max_length=254, default=None, blank=True, null=True)
    maintenance = models.CharField(max_length=54, default=None, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="images/")
    favicon = models.ImageField(blank=True, null=True, upload_to="images/")
    signup_msg = models.CharField(blank=True, null=True, max_length=500)
    login_auth_msg = models.CharField(blank=True, null=True, max_length=500)
    password_reset_msg = models.CharField(blank=True, null=True, max_length=500)
    phone = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.title

class CurrentPrice(models.Model):
    currency = models.CharField(blank=True, null=True, max_length=255)
    ntc = models.CharField(blank=True, null=True, max_length=255)
    usd = models.CharField(blank=True, null=True, max_length=255)
    amount = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.currency
