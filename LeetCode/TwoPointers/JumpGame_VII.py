# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, 
# which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

    # i + minJump <= j <= min(i + maxJump, s.length - 1), and
    # s[j] == '0'.

# Return true if you can reach index s.length - 1 in s, or false otherwise.

def canReach(s, minJump, maxJump):
    dp = [ch == '0' for ch in s]
    pre = 0
    for i in range(1, len(s)):
        if i >= minJump: 
            pre += dp[i - minJump]
        if i > maxJump:
            pre -= dp[i - maxJump - 1]
        dp[i] &= pre > 0
    return dp[-1]

s = "01101110"
minJump = 2
maxJump = 3

print(canReach(s, minJump, maxJump))