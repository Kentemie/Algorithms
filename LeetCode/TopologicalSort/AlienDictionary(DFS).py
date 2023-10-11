# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are 
# sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new 
# language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

def alienOrder(words):
    adj = { char: set() for word in words for char in word }

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break 
    
    visited = {} # False - visited, True - char in the current path
    res = []

    # when DFS return true, means there is a cycle
    def DFS(char):
        if char in visited:
            return visited[char]
    
        visited[char] = True

        for nei in adj[char]:
            if DFS(nei):
                return True
            
        visited[char] = False
        res.append(char)

    for char in adj:
        if DFS(char):
            return ""
        
    return "".join(res[::-1])

words = ["wrt","wrf","er","ett","rftt"]
# words = ["z","x","z"]
# words = ["z","x"]
# words = ["ab", "abc"]
# words = ["abc", "ab"]

print(alienOrder(words))
