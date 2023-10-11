# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to 
# right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    res = []
    if not root:
        return res
    lvl = 0
    queue = deque([root])
    while queue:
        res.append([])
        for _ in range(len(queue)):
            node = queue.popleft()
            res[lvl].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        lvl += 1
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))