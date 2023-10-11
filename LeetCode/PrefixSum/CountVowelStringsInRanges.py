# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) 
# of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

def vowelStrings(words, queries):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    prefixSum = [0] * (len(words) + 1)

    for i in range(1, len(words) + 1):
        prefixSum[i] += prefixSum[i - 1]
        if words[i - 1][-1] in vowels and words[i - 1][0] in vowels:
            prefixSum[i] += 1

    res = []

    for query in queries:
        res.append(prefixSum[query[1] + 1] - prefixSum[query[0]])

    return res

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

# words = ["a","e","i"]
# queries = [[0,2],[0,1],[2,2]]

print(vowelStrings(words, queries))
