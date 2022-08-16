from django.db import models

# Create your models here.
class Messages(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    receiver_id = models.IntegerField(blank=True, null=True)
    sender_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(blank=True, null=True, max_length=255)
    photo = models.ImageField(blank=True, null=True, upload_to="messages/")
    seen = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()
