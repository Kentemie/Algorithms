# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are 
# multiple valid strings, return any of them.

# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

# def SCS(word1, word2):

#     dp = [[[]] * (len(word1) + 1) for _ in range(len(word2) + 1)]

#     for row in range(1, len(word2) + 1):
#         for col in range(1, len(word1) + 1):
#             if word2[row - 1] == word1[col - 1]:
#                 dp[row][col] = dp[row - 1][col - 1].copy()
#                 dp[row][col].append(word2[row - 1])
#             else:
#                 dp[row][col] = dp[row][col - 1] if len(dp[row][col - 1]) > len(dp[row - 1][col]) else dp[row - 1][col]
        
#     return dp[-1][-1]

# # str1 = "abac"
# # str2 = "cab"
# str1 = "aaaaaaaa"
# str2 = "aaaaaaaa"

# subs = SCS(str1, str2)

# flag1, flag2 = False, False
# i, j, k = 0, 0, 0
# superSubs = []

# while i < len(str1) and j < len(str2) and k < len(subs):
#     if flag1 and flag2:
#         superSubs.append(subs[k])
#         i += 1
#         j += 1
#         k += 1
#         flag1, flag2 = False, False
#         continue
#     if str1[i] != subs[k]:
#         superSubs.append(str1[i])
#         i += 1
#     else:
#         flag1 = True
#     if str2[j] != subs[k]:
#         superSubs.append(str2[j])
#         j += 1
#     else:
#         flag2 = True

# superSubs.append(str1[i:])
# superSubs.append(str2[j:])

# print("".join(superSubs))


def SCS(str1, str2):
    n, m = len(str2), len(str1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    superSubs = ""
    i, j = m, n

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            superSubs = str1[i - 1] + superSubs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            superSubs = str1[i - 1] + superSubs
            i -= 1
        else:
            superSubs = str2[j - 1] + superSubs
            j -= 1

    while i > 0:
        superSubs = str1[i - 1] + superSubs
        i -= 1
    while j > 0:
        superSubs = str2[j - 1] + superSubs
        j -= 1
    
    return superSubs

str1 = "abac"
str2 = "cab"

print(SCS(str1, str2))