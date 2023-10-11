# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may 
# not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    res = 0
    def DFS(root):
        nonlocal res 
        if not root:
            return -1
        left = DFS(root.left)
        right = DFS(root.right)
        res = max(res, left + right + 2)
        return 1 + max(left, right)
    DFS(root)
    return res 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))