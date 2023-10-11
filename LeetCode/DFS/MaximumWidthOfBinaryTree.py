# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
# where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are
# also counted into the length calculation.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def DFS(node, depth, idx):
    global max_width
    if not node:
        return 
    if depth not in lvlHeadIdx:
        lvlHeadIdx[depth] = idx

    max_width = max(max_width, idx - lvlHeadIdx[depth] + 1)

    DFS(node.left, depth + 1, idx * 2)
    DFS(node.right, depth + 1, idx * 2 + 1)

max_width = 0
lvlHeadIdx = {}

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8)

DFS(root, 0, 1)

print(max_width)