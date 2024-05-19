from django.db import models


class OperationCount(models.Model):
    addition_count = models.PositiveIntegerField(default=0)
    subtraction_count = models.PositiveIntegerField(default=0)
    total_expressions = models.PositiveIntegerField(default=0)

    @property
    def average_operations(self):
        if self.total_expressions == 0:
            return 0
        return (self.addition_count + self.subtraction_count) / self.total_expressions
