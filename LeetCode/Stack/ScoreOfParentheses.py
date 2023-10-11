# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

    # () has score 1.
    # AB has score A + B, where A and B are balanced parentheses strings.
    # (A) has score 2 * A, where A is a balanced parentheses string.

def scoreOfParentheses(s):
    stack = [0]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(0)
        else:
            d = stack.pop()
            stack[-1] += max(d * 2, 1)
    return stack.pop()

s = "((()))((()))"
s = "(()(()))"

print(scoreOfParentheses(s))