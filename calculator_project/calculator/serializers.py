from rest_framework import serializers


class ExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField()
