# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after 
# removing k digits from num.

def removeKdigits(num, k):
    digits = list(num)
    stack = []
    for i in range(len(digits)):
        while k > 0 and stack and digits[i] < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digits[i])
    finalNum = stack[:-k] if k else stack
    return "".join(finalNum).lstrip('0') or '0'

num = "1432219"
k = 3
# num = "10200"
# k = 1


print(removeKdigits(num, k))