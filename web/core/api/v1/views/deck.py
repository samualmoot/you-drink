from rest_framework import viewsets
from web.core import models


class DeckViewSet(viewsets.ModelViewSet):
    queryset = models.Deck.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)