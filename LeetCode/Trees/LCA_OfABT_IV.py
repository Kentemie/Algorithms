# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes
# in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the 
# lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A 
# descendant of a node x is a node y that is on the path from node x to some leaf node.

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def lowestCommonAncestor(root, nodes):
    nodes = set(nodes)

    def DFS(node):
        if not node:
            return None
        if node.val in nodes:
            return node
        
        left, right = DFS(node.left), DFS(node.right)
        
        if left and right:
            return node
        return left or right
    
    return DFS(root).val

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
nodes = [7,6,2,4,0]

print(lowestCommonAncestor(root, nodes))