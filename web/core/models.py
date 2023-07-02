from django.db import models


class Deck(models.Model):
    deck_type = models.CharField(max_length=2048)


class Card(models.Model):
    message = models.CharField(max_length=2048)
    drink_amount = models.IntegerField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, default=None)