# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
# truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
# [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if 
# the quotient is strictly less than -2^31, then return -2^31.


def divide(dividend, divisor):
    sign = (dividend > 0) ^ (divisor > 0)
    temp = 0
    quotient = 0

    dividend, divisor = abs(dividend), abs(divisor)

    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += (divisor << i)
            quotient |= 1 << i
    
    quotient = quotient * (-1) if sign else quotient
    
    if quotient < -(2**31):
        return -(2**31)
    elif quotient > 2**31 - 1:
        return 2**31 - 1
    return quotient


dividend = 10
divisor = 3

dividend = 7
divisor = -3

print(divide(dividend, divisor))