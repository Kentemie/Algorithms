# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. 
# The process of naming a company is as follows:

    # Choose 2 distinct names from ideas, call them ideaA and ideaB.
    # Swap the first letters of ideaA and ideaB with each other.
    # If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB,
    # separated by a space) is a valid company name.
    # Otherwise, it is not a valid name.

# Return the number of distinct valid names for the company.


from collections import defaultdict

def distinctNames(ideas):
    wordMap = defaultdict(set)
    res = 0
    
    for word in ideas:
        wordMap[word[0]].add(word[1:])

    for ch1 in wordMap:
        for ch2 in wordMap:
            if ch1 == ch2:
                continue
            intersecting_suffixes = len(wordMap[ch1] & wordMap[ch2])
            distinct1 = len(wordMap[ch1]) - intersecting_suffixes
            distinct2 = len(wordMap[ch2]) - intersecting_suffixes
            res += distinct1 * distinct2

    return res


ideas = ["coffee","donuts","time","toffee"]

print(distinctNames(ideas))