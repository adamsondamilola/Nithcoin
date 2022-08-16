from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    firstname = models.CharField(blank=True, null=True, max_length=255)
    lastname = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(max_length=150, default=None, blank=True, null=True)
    mobile = models.CharField(max_length=25, default=None, blank=True, null=True)
    altmobile = models.CharField(max_length=25, default=None, blank=True, null=True)
    profile = models.ImageField(blank=True, null=True, upload_to="users/")
    cover = models.ImageField(blank=True, null=True, upload_to="users/")
    full_face = models.ImageField(blank=True, null=True, upload_to="users/")
    id_card = models.ImageField(blank=True, null=True, upload_to="users/")
    proof_of_residence = models.ImageField(blank=True, null=True, upload_to="users/")
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id

class Referrals(models.Model):
    invitee = models.IntegerField(blank=True, null=True)
    invited = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_verified = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.invitee

class Cards(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    card_id = models.CharField(max_length=255, unique=True)
    card_pin = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.user_id
