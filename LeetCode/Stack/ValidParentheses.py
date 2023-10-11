# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in s:
        if char in brackets:
            top = stack.pop() if stack else "#"
            if brackets[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

s = ")"
s = "()[]{}"
s = "(((({{{}]}))))"

print(isValid(s))