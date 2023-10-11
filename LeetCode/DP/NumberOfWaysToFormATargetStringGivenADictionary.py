# You are given a list of strings of the same length words and a string target.

# Your task is to form target using the given words under the following rules:

#     target should be formed from left to right.
#     To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
#     Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k.
#     In other words, all characters to the left of or at index k become unusuable for every string.
#     Repeat the process until you form the string target.

# Notice that you can use multiple characters from the same string in words provided the conditions above are met.

# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.


def numWays(words, target):
    MOD = 10 ** 9 + 7
    chars_counter = [[0] * 26 for _ in range(len(words[0]))] # (index, char) -> count among all words 

    for word in words:
        for idx, char in enumerate(word):
            chars_counter[idx][ord(char) - 97] += 1

    dp = [[-1] * len(words[0]) for _ in range(len(target))]

    # i = index of target, k = index of words[j][k]
    def DFS(i, k):
        if i == len(target):
            return 1
        if k == len(words[0]):
            return 0
        if dp[i][k] != -1:
            return dp[i][k]
        
        char = target[i]
        dp[i][k] = DFS(i, k + 1) # skip k position
        dp[i][k] += chars_counter[k][ord(char) - 97] * DFS(i + 1, k + 1)
        return dp[i][k] % MOD
    
    return DFS(0, 0)



words = ["acca","bbbb","caca"]
target = "aba"

print(numWays(words, target))