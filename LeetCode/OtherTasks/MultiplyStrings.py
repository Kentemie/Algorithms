# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    
    n = len(num1) + len(num2)
    res = [0] * n

    first_number = num1[::-1]
    second_number = num2[::-1]

    for place2, digit2 in enumerate(second_number):
        for place1, digit1 in enumerate(first_number):
            num_zeroes = place1 + place2

            carry = res[num_zeroes]
            product = int(digit1) * int(digit2) + carry

            res[num_zeroes] = product % 10
            res[num_zeroes + 1] += product // 10

    if res[-1] == 0:
        res.pop()
    
    return "".join(str(digit) for digit in reversed(res))

num1 = "123"
num2 = "456"

print(multiply(num1, num2))