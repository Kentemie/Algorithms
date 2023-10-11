# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

s = ""
s = "))))))))))(((()))))()))))))(((())"

stack = []
stack.append(-1)
maxLen = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if len(stack) == 0:
            stack.append(i)
        else:
            maxLen = max(maxLen, i - stack[-1])

print(maxLen)
