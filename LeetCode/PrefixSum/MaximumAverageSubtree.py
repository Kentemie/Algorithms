# Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10^-5 of
# the actual answer will be accepted.

# A subtree of a tree is any node of that tree plus all its descendants.

# The average value of a tree is the sum of its values, divided by the number of nodes.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maximumAverageSubtree(root):
    maxAVG = 0
    def DFS(root):
        nonlocal maxAVG
        if not root:
            return 0, 0
        
        left_subtree = DFS(root.left)
        right_subtree = DFS(root.right)
        nodesCnt = left_subtree[1] + right_subtree[1] + 1
        currSum = root.val + left_subtree[0] + right_subtree[0]
        maxAVG = max(maxAVG, currSum / nodesCnt)
        return currSum, nodesCnt

    DFS(root)
    return maxAVG

root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(1)

print(maximumAverageSubtree(root))