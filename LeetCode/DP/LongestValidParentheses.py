# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

s = "))))))))))(((()))))()))))))(((())"

dp = [0] * len(s)
maxLen = 0

for i in range(1, len(s)):
    if s[i] == ')':
        if s[i - 1] == '(':
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
            dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
        maxLen = max(maxLen, dp[i])
print(maxLen)