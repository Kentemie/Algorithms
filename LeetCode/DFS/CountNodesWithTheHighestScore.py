# There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed 
# integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, 
# parents[0] == -1.

# Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. 
# The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score 
# of the node is the product of the sizes of all those subtrees.

# Return the number of nodes that have the highest score.

def countHighestScoreNodes(parents):
    n = len(parents)
    graph = [[] for _ in range(n)]

    for node, parent in enumerate(parents):
        if node:
            graph[parent].append(node)

    print(graph)

    scores = [1] * n

    def DFS(node):
        res = 1
        for child in graph[node]:
            val = DFS(child)
            res += val
            scores[node] *= val
        if node:
            scores[node] *= (n - res)
        return res

    DFS(0)
    print(scores)
    return scores.count(max(scores))

parents = [-1,2,0,2,0]
# 3
# parents = [-1,2,0] 
# 2

print(countHighestScoreNodes(parents))