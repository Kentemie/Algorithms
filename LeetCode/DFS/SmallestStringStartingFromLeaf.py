# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# As a reminder, any shorter prefix of a string is lexicographically smaller.

    # For example, "ab" is lexicographically smaller than "aba".

# A leaf of a node is a node that has no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallestFromLeaf(root):
    ans = "~"

    def DFS(root, currStr):
        nonlocal ans
        if root:    
            currStr.append(chr(root.val + 97))

            if not root.left and not root.right:
                ans = min(ans, "".join(reversed(currStr)))
            
            DFS(root.left, currStr)
            DFS(root.right, currStr)

            currStr.pop()
    
    DFS(root, [])

    return ans

# root = TreeNode(0)
# root.left = TreeNode(1)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)

root = TreeNode(25)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(2)

print(smallestFromLeaf(root))