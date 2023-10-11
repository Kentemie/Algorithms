# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

def calculate(s):
    idx = -1

    def estimate(operand, sign):
        nonlocal idx
        result = 0

        while idx < len(s) - 1:
            idx += 1
            char = s[idx]

            if char == ' ':
                continue
            elif char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '(':
                operand = estimate(0, 1)
            elif char == ')':
                return result + operand * sign
            else:
                result += operand * sign
                sign = 1 if char == '+' else -1
                operand = 0

        return result + operand * sign
    
    return estimate(0, 1)

s = "1 + 1"
s = " 2-1 + 2 "
s = "(1+(4+5+2)-3)+(6+8)"
s = "- (3 + (4 + 5))"

print(calculate(s))