# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in
# this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on
# the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def DFS(root):
    if not root:
        return [0, 0]
    left = DFS(root.left)
    right = DFS(root.right)

    rob = root.val + left[1] + right[1]
    do_not_rob = max(left) + max(right)

    return [rob, do_not_rob]

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(max(DFS(root)))