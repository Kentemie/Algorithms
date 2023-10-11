from collections import deque

def alienOrder(words):
    adj = { char: set() for word in words for char in word }
    inDegree = { char: 0 for word in words for char in word }

    for w1, w2 in zip(words, words[1:]):
        for ch1, ch2 in zip(w1, w2):
            if ch1 != ch2:
                if ch2 not in adj[ch1]:
                    adj[ch1].add(ch2)
                    inDegree[ch2] += 1
                break
        else:
            if len(w2) < len(w1):
                return ""
                
    res = []
    queue = deque([char for char in inDegree if inDegree[char] == 0])

    while queue:
        ch1 = queue.popleft()
        res.append(ch1)
        for ch2 in adj[ch1]:
            inDegree[ch2] -= 1
            if inDegree[ch2] == 0:
                queue.append(ch2)

    # If not all letters are in res, that means there was a cycle and so no valid ordering.
    if len(res) < len(inDegree):
        return ""
    return "".join(res)


words = ["wrt","wrf","er","ett","rftt"]
# words = ["z","x","z"]
# words = ["z","x"]
# words = ["ab", "abc"]
# words = ["abc", "ab"]
words = ["ac","ab","zc","zb"]
words = ["qb","qts","qs","qa","s"]

print(alienOrder(words))