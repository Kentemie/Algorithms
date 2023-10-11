# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

    # For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    def DFS(root, num):
        if not root:
            return 0
        
        num = num * 10 + root.val
        
        if not root.left and not root.right:
            return num
        return DFS(root.left, num) + DFS(root.right, num)

    return DFS(root, 0)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sumNumbers(root))