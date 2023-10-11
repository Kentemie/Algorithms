# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected 
# graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that 
# there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
# When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum 
# height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

def findMinHeightTrees(n, edges):

    if n <= 2:
        return [i for i in range(n)]

    graph = [set() for _ in range(n)]

    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])


    # Initialize the first layer of leaves
    leaves = []
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.append(i)

    remaining_nodes = n
    # Trim the leaves until reaching the centroids
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []

        while leaves:
            leaf = leaves.pop()
            # the only neighbor left for the leaf node
            neighbor = graph[leaf].pop()
            # remove the only edge left
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves
    
    return leaves

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

print(findMinHeightTrees(n, edges))