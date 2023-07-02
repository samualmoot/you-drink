from django.http import HttpResponse
from rest_framework import viewsets
from web.core import models


def index(request):
    return HttpResponse("Hello, world. You're at the card index.")


class DeckViewSet(viewsets.ModelViewSet):
    queryset = models.Deck.objects.all()