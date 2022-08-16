from django.db import models

#data models
from site_settings.models import CurrentPrice
# Create your models here.
class Vendors(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    firstname = models.CharField(blank=True, null=True, max_length=255)
    lastname = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(max_length=150, default=None, blank=True, null=True)
    mobile = models.CharField(max_length=25, default=None, blank=True, null=True)
    whatsapp = models.CharField(max_length=25, default=None, blank=True, null=True)
    profile = models.ImageField(blank=True, null=True, upload_to="vendors/")
    cover = models.ImageField(blank=True, null=True, upload_to="vendors/")
    full_face = models.ImageField(blank=True, null=True, upload_to="vendors/")
    id_card = models.ImageField(blank=True, null=True, upload_to="vendors/")
    proof_of_residence = models.ImageField(blank=True, null=True, upload_to="vendors/")
    status = models.IntegerField(blank=True, null=True)
    minimum = models.FloatField(blank=True, null=True)
    selling_at = models.FloatField(blank=True, null=True)
    buying_at = models.FloatField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id

    def selling_att(self):
        current_price = CurrentPrice.objects.last()
        curprice = int(current_price)
        sell_usd = (int(self.selling_at)/100 * curprice) + curprice
        return sell_usd

    def buying_att(self):
        current_price = CurrentPrice.objects.last()
        curprice = int(current_price)
        buy_usd = (int(self.buying_at)/100 * curprice) + curprice
        return buy_usd


class PaymentMethods(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    method = models.CharField(blank=True, null=True, max_length=255)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id
