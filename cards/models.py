import hashlib

from django.db import models
from django.db.models.signals import post_save


class CardQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(locked=False)


class CardManager(models.Manager):
    def get_queryset(self):
        return CardQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# Create your models here.
class Card(models.Model):
    number = models.TextField(max_length=16, unique=True)
    password = models.TextField(max_length=256)
    locked = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)

    objects = CardManager()

    def __str__(self):
        return self.number


def card_item_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        password = instance.password
        password = hashlib.md5(password.encode())
        instance.password = password.hexdigest()
        instance.save()

post_save.connect(card_item_post_save_receiver, sender=Card)