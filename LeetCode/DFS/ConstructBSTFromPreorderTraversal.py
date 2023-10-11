# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), 
# construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than 
# Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder):
    def DFS(low = float('-inf'), high = float('inf')):
        nonlocal idx
        if idx == n:
            return None
        val = preorder[idx]
        if high <= val or val <= low:
            return None
        idx += 1
        node = TreeNode(val)
        node.left = DFS(low, val)
        node.right = DFS(val, high)
        return node

    idx = 0
    n = len(preorder)
    return DFS()

preorder = [8,5,1,7,10,12]

print(bstFromPreorder(preorder))