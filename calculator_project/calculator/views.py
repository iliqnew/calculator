import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExpressionSerializer
from .services.parser import ExpressionParser, InvalidExpressionException
from .models import OperationCount


class CalculationView(APIView):
    def post(self, request):
        request_process_time_start = time.time()
        serializer = ExpressionSerializer(data=request.data)
        if serializer.is_valid():
            expression = serializer.validated_data["expression"]
            parser = ExpressionParser()
            try:
                evaluation_time_start = time.time()
                result = parser.evaluate(expression)
                evaluation_time = time.time() - evaluation_time_start
                # Trackers
                operation_count, _ = OperationCount.objects.get_or_create(id=1)
                addition_count = expression.count("+")
                subtraction_count = expression.count("-")

                operation_count.addition_count += addition_count
                operation_count.subtraction_count += subtraction_count
                operation_count.total_expressions += 1
                operation_count.save()

                average_operations = operation_count.average_operations

                return Response(
                    {
                        "result": result,
                        "addition_count": addition_count,
                        "subtraction_count": subtraction_count,
                        "average_operations": average_operations,
                        "evaluation_time": evaluation_time,
                        "request_process_time": time.time()
                        - request_process_time_start,
                    },
                    status=status.HTTP_200_OK,
                )
            except InvalidExpressionException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
