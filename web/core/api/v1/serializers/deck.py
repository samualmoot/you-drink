from rest_framework import serializers

class DeckSerializer(serializers.Serializer):
    deck_type = serializers.CharField(max_length=30)