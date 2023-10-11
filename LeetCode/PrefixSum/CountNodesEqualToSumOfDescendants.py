# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the sum of the values
# of its descendants.

# A descendant of a node x is any node that is on the path from node x to some leaf node. The sum is considered to be 0 if the
# node has no descendants.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def equalToDescendants(root):
    def DFS(root):
        if not root:
            return 0

        left_subtree = DFS(root.left)
        right_subtree = DFS(root.right)
        if left_subtree + right_subtree == root.val:
            res.append(root.val)
        currSum = root.val + left_subtree + right_subtree
        return currSum
    
    res = []
    DFS(root)
    return res

root = TreeNode(10)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)

print(equalToDescendants(root))