# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes),
# where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that 
# level are also counted into the length calculation.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BFS(root):
    queue = deque([(root, 1)])
    ans = 0
    while queue:
        n = len(queue)
        lvlHeadIdx = queue[0][1]
        for _ in range(n):
            node, idx = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * idx))
            if node.right:
                queue.append((node.right, 2 * idx + 1))
        ans = max(ans, idx - lvlHeadIdx + 1)

    return ans


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8)

print(BFS(root))