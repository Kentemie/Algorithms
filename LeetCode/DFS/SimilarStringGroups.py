# Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most 
# two letters (in distinct positions) within the string X.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not 
# similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts"
# are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only 
# if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?


def DFS(i, graph, visited):
    visited[i] = True
    for nei in graph[i]:
        if not visited[nei]:
            DFS(nei, graph, visited)

def is_similar(ss1, ss2):
    diff = 0
    for i in range(len(ss1)):
        if ss1[i] != ss2[i]:
            diff += 1
        
    return diff == 0 or diff == 2

def numSimilarGroups(strs):
    n = len(strs)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            DFS(i, graph, visited)
            count += 1

    return count

strs = ["tars","rats","arts","star"]
strs = ["omv","ovm"]

print(numSimilarGroups(strs))