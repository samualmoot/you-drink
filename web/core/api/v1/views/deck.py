from rest_framework import viewsets
from rest_framework.response import Response
from web.core import models
from web.core.api.v1.serializers.deck import DeckSerializer
from django.shortcuts import get_object_or_404


class DeckViewSet(viewsets.ModelViewSet):
    queryset = models.Deck.objects.all()

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        serializer = DeckSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        deck = get_object_or_404(self.queryset, pk=pk)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)
        