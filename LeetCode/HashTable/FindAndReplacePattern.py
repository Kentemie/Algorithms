# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the 
# answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the 
# pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
# and no two letters map to the same letter.

# def matching(word):
#     word_mapping = {}

#     for i in range(len(word)):
#         word_mapping[word[i]] = i

#     if len(word_mapping) != len(pattern_mapping):
#         return False
    
#     for letter1, letter2 in zip(pattern_mapping.keys(), word_mapping.keys()):
#         if pattern_mapping[letter1] != word_mapping[letter2]:
#             return False

#     return True


# pattern = 'abb'
# words = ["abc","deq","mee","aqq","dkd","ccc"]

# pattern = "baba"
# words = ["badc","abab","dddd","dede","yyxx"]

# pattern_mapping = {}

# for i in range(len(pattern)):
#     pattern_mapping[pattern[i]] = i

# res = []

# for word in words:
#     if matching(word):
#         res.append(word)

# print(res)


def findAndReplacePattern(words, pattern):
    def match(word):
        m1, m2 = {}, {}
        return all((m1.setdefault(i, j), m2.setdefault(j, i)) == (j, i) for i, j in zip(word, pattern))
    
    return list(filter(match, words))

pattern = "baba"
words = ["badc","abab","dddd","dede","yyxx"]

print(findAndReplacePattern(words, pattern))