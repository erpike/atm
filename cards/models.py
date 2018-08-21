import hashlib


from django.db import models
from django.db.models.signals import pre_save


# Create your models here.
class Card(models.Model):
    number = models.TextField(max_length=16)
    password = models.TextField(max_length=256)
    status = models.BooleanField(default=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.number


def card_item_pre_save_receiver(sender, instance, *args, **kwargs):
    password = instance.password
    password = hashlib.md5(password.encode())
    instance.password = password.hexdigest()

pre_save.connect(card_item_pre_save_receiver, sender=Card)