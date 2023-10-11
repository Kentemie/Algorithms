# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     # The left subtree of a node contains only nodes with keys less than the node's key.
#     # The right subtree of a node contains only nodes with keys greater than the node's key.
#     # Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float('-inf'), float('inf'))


# class Solution:
#     def isValidBST(self, root) -> bool:
#         def inOrder(root):
#             if not root:
#                 return True
#             if not inOrder(root.left):
#                 return False
#             if root.val <= self.prev:
#                 return False
#             self.prev = root.val
#             return inOrder(root.right)
        
#         self.prev = float('-inf')
#         return inOrder(root)
            