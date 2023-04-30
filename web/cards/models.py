from django.db import models

class Cards(models.Model):
    message = models.CharField(max_length=2048)
    drink_amount = models.IntegerField()