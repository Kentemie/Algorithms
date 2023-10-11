# # Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more 
# # dictionary words.
# # Note that the same word in the dictionary may be reused multiple times in the segmentation.

# def wordBreak(s, wordDict, start):
#     if start == len(s):
#         return True
#     if start in memo: 
#         return False
#     for end in range(start+1, len(s) + 1):
#         if s[start:end] in wordDict and wordBreak(s, wordDict, end):
#             return True
#     memo.add(start)
#     return False

# s = "applepenapple"
# wordDict = ["apple","pen"]

# wordDict = set(wordDict)
# memo = set()

# print(wordBreak(s, wordDict, 0))


# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# dp = [False] * len(s)

# for i in range(len(s)):
#     for word in wordDict:
#         if i >= len(word) - 1 and (dp[i - len(word)] or i == len(word) - 1):
#             if s[i - len(word) + 1 : i + 1] == word:
#                 dp[i] = True
#                 break

# print(dp[-1])


def dp(i):
    if i < 0:
        return True
    
    for word in wordDict:
        if i >= len(word) - 1 and dp(i - len(word)):
            if s[i - len(word) + 1 : i + 1] == word:
                return True
            
    return False 


s = "leetcode"
wordDict = ["leet","code"]

print(dp(len(s) - 1))