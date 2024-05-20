import re
import math


class InvalidExpressionException(Exception):
    pass


class ExpressionParser:
    def __init__(self):
        self.operators = set("+-*/^")
        self.digits = set("0123456789")
        self.brackets = {"(": ")", "[": "]"}
        self.allowed_chars = set("0123456789+-*/^%!().[] ")

    @staticmethod
    def in_limits(ind: int, expression: str) -> bool:
        return ind > 0 and ind < len(expression) - 1

    def validate_brackets(self, expression: str) -> bool:

        # general/quick brackets check. Count and compare opening and closing brackets
        for open, close in self.brackets.items():
            if expression.count(open) != expression.count(close):
                raise InvalidExpressionException("Brackets are not balanced")

        # check for bracket balance and neighbours
        s = ""
        for i, char in enumerate(expression):
            if char not in set(self.brackets.keys()) | set(self.brackets.values()):
                continue

            openning, closing = next(b for b in self.brackets.items() if char in b)

            left = expression[i - 1] if self.in_limits(i - 1, expression) else None
            right = expression[i + 1] if self.in_limits(i + 1, expression) else None

            # opening bracket guardian
            if char == openning:
                if not all(
                    [
                        (left in set("([ ") | self.operators or left is None),
                        (right in set("([ ") | self.digits or right is not None),
                    ]
                ):
                    raise InvalidExpressionException(
                        "Invalid opening bracket neighbours"
                    )
                s += char
                continue

            # closing bracket guardian
            if char == closing:
                if not all(
                    [
                        (left in set("]) ") | self.digits or left is not None),
                        (right in set("]) ") | self.operators or right is None),
                    ]
                ):
                    raise InvalidExpressionException(
                        "Invalid closing bracket neighbours"
                    )
                if any(
                    [
                        # doesn't have a previous opening bracket
                        s == "",
                        # last bracket is not the oppening one of this type
                        s[-1] != openning,
                    ]
                ):
                    raise InvalidExpressionException("Brackets are not balanced")
                s = s[:-1]

        return len(s) == 0

    def validate(self, expression: str):
        # disallow empty expressions
        if not expression.strip():
            raise InvalidExpressionException("Expression cannot be empty")
        # disallow expressions with characters that are not allowed
        if not all(char in self.allowed_chars for char in expression):
            raise InvalidExpressionException("Invalid characters in expression")
        # disallow expressions with brackets that are not balanced
        if not self.validate_brackets(expression):
            raise InvalidExpressionException("Expression has unbalanced brackets")

        # Additional validation rules can be added here

    def evaluate(self, expression):
        self.validate(expression)

        try:
            # Replace ^ with ** for exponentiation
            expression = expression.replace("^", "**")
            print(expression)
            # replace ! with math.factorial
            real_number_pattern = r"(\d+)"
            expression = re.sub(
                f"{real_number_pattern}!", r"math.factorial(\1)", expression
            )
            print(expression)
            # replace '[' and ']' with '(' and ')'
            expression = expression.replace("[", "(").replace("]", ")")
            print(expression)
            # replace % with percentage (a / 100 * b)
            expression = re.sub(
                f"{real_number_pattern}\s?%\s?{real_number_pattern}",
                r"\1/100*\2",
                expression,
            )
            print(expression)

            # Evaluate the expression safely
            result = eval(
                expression,
                {"__builtins__": None},
                {
                    "math": math,
                },
            )
            return result
        except Exception as e:
            raise InvalidExpressionException(str(e))
