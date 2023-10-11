# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

def maxPathSum(root):
    res = float("-inf")

    def DFS(node):
        nonlocal res
        if not node:
            return 0
        
        leftPart = max(DFS(node.left), 0)
        rightPart = max(DFS(node.right), 0)
        res = max(res, leftPart + rightPart + node.val)

        return max(leftPart, rightPart) + node.val
    
    DFS(root)

    return res
    
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxPathSum(root))