from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=200, default=None)
    type = models.CharField(max_length=30, default=None)


class Card(models.Model):
    message = models.CharField(max_length=2048)
    drink_amount = models.IntegerField(default=1)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=30, default=None)