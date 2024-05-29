import re
import math


class InvalidExpressionException(Exception):
    pass


class ExpressionParser:
    real_number_pattern_t = r"(?P<real_number_{}>(?P<neg_{}>\(\s?-\s?)?(?P<float_{}>(?P<int_{}>\d+)?(?P<decimal_{}>(?(int_{})(\.\d+)?|(\.\d+))))(?(neg_{})\)|))"

    def evaluate(self, expression):
        # self.validate(expression)

        real_number_pattern_a = self.real_number_pattern_t.replace("{}", "a")
        real_number_pattern_b = self.real_number_pattern_t.replace("{}", "b")
        # Replace ^ with ** for exponentiation
        expression = expression.replace("^", "**")
        print(expression)
        # replace ! with math.factorial
        expression = re.sub(
            f"{real_number_pattern_a}!",
            r"math.factorial(\g<real_number_a>)",
            expression,
        )
        print(expression)
        # replace '[' and ']' with '(' and ')'
        expression = expression.replace("[", "(").replace("]", ")")
        print(expression)
        # replace % with percentage (a / 100 * b)
        expression = re.sub(
            f"{real_number_pattern_a}\s?%\s?{real_number_pattern_b}",
            r"\g<real_number_a>/100*\g<real_number_b>",
            expression,
        )
        print(expression)

        return self.evaluate_recursive(expression)

    def evaluate_recursive(self, expression):
        for i, char in enumerate(expression):
            if char == "(":
                sub_expression = ""
                for j, char_2 in enumerate(expression[i + 1 :], start=i + 1):
                    if char_2 == ")":
                        break
                    sub_expression += char_2
                else:
                    raise InvalidExpressionException("Missing closing bracket")
                sub_result = self.evaluate_recursive(sub_expression)
                sub_result = f"({sub_result})" if sub_result < 0 else f"{sub_result}"
                print(i, j, sub_result)
                expression = expression[:i] + sub_result + expression[j + 1 :]
                print(expression)
                break

        try:
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
