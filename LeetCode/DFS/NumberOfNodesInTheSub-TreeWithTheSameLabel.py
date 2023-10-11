# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to 
# n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a 
# lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label
# as node i.

# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

def countSubTrees(n, edges, labels):
    res = [0] * n

    def DFS(node, parent, nodes, labels):
        curr = [0] * 26
        curr[ord(labels[node]) - ord('a')] += 1

        for child in nodes[node]:
            if child == parent:
                continue
            childCurr = DFS(child, node, nodes, labels)
            curr = list(map(sum, zip(curr, childCurr)))
        
        res[node] = curr[ord(labels[node]) - ord('a')]
        return curr
    
    nodes = [[] for _ in range(n)]

    for edge in edges:
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])

    DFS(0, -1, nodes, labels)

    return res


# n = 7
# edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
# labels = "abaedcd"

# n = 1
# edges = []
# labels = "a"

n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"

# n = 5
# edges = [[0,1],[0,2],[1,3],[0,4]]
# labels = "aabab"

print(countSubTrees(n, edges, labels))