# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    ans = []

    def backtracking(currStr, cntLeft, cntRight):
        if len(currStr) == 2 * n:
            ans.append("".join(currStr))
        if cntLeft < n:
            currStr.append('(')
            backtracking(currStr, cntLeft + 1, cntRight)
            currStr.pop()
        if cntRight < cntLeft:
            currStr.append(')')
            backtracking(currStr, cntLeft, cntRight + 1)
            currStr.pop()
    
    backtracking([], 0, 0)

    return ans

n = 3

print(generateParenthesis(n))