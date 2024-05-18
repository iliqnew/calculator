from rest_framework import serializers


class CalculationSerializer(serializers.Serializer):
    operation = serializers.ChoiceField(
        choices=["add", "subtract", "multiply", "divide"]
    )
    a = serializers.FloatField()
    b = serializers.FloatField()
