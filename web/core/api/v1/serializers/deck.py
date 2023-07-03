from rest_framework import serializers

class DeckSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=200)