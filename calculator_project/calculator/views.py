from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationSerializer
from .services.calculator import Calculator


class CalculationView(APIView):
    def post(self, request):
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            operation = serializer.validated_data["operation"]
            a = serializer.validated_data["a"]
            b = serializer.validated_data["b"]

            calculator = Calculator()
            try:
                if operation == "add":
                    result = calculator.add(a, b)
                elif operation == "subtract":
                    result = calculator.subtract(a, b)
                elif operation == "multiply":
                    result = calculator.multiply(a, b)
                elif operation == "divide":
                    result = calculator.divide(a, b)

                return Response({"result": result}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
