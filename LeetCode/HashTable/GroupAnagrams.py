# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

# def groupAnagrams(strs):
#     res = []
#     hashMap = {}
    
#     for word in strs:
#         key = "".join(sorted(word))
#         if key in hashMap:
#             hashMap[key].append(word)
#         else:
#             hashMap[key] = [word]
#     for anagrams in hashMap.values():
#         res.append(anagrams)

#     return res


from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        ans[tuple(count)].append(word)
    
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))