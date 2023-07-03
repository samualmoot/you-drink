from rest_framework import serializers

class CardSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=30)
    message = serializers.CharField(max_length=2048)
    drink_amount = serializers.IntegerField(min=1, max=6)