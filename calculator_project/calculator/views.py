from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExpressionSerializer
from .services.parser import ExpressionParser, InvalidExpressionException


class CalculationView(APIView):
    def post(self, request):
        serializer = ExpressionSerializer(data=request.data)
        if serializer.is_valid():
            expression = serializer.validated_data["expression"]
            parser = ExpressionParser()
            try:
                result = parser.evaluate(expression)
                return Response({"result": result}, status=status.HTTP_200_OK)
            except InvalidExpressionException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
