# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as 
# far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
        else:
            while queue:
                if queue.popleft():
                    return False
    
    return True