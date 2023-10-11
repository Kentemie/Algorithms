# The idea is to use recursion and keep track of the maximum level also. And traverse the tree in a manner that the right
# subtree is visited before the left subtree.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightViewUtil(root, lvl, maxLvl):
    if not root:
        return 

    if maxLvl[0] < lvl:
        res.append(root.val)
        maxLvl[0] = lvl
    
    rightViewUtil(root.right, lvl + 1, maxLvl)
    rightViewUtil(root.left, lvl + 1, maxLvl)


def rightView(root):
    maxLvl = [0]
    rightViewUtil(root, 1, maxLvl)


def rightViewLvlOrderTraversal(root):
    if not root:
        return
    
    queue = deque([root])

    while queue:
        n = len(queue)
        while n > 0:
            n -= 1
            node = queue.popleft()
            if n == 0:
                ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                

res = []
ans = []

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)

rightView(root)
rightViewLvlOrderTraversal(root)

print(ans)
print(res)

