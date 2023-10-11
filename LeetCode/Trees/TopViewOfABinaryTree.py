from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):
    res = []
    
    queue = deque([(root, 0)])
    
    left = []
    right = []

    leftMin, rightMax = 0, 0

    while queue:
        node, hd = queue.popleft()

        if leftMin > hd:
            left.append(node.val)
            leftMin = hd
        elif rightMax < hd:
            right.append(node.val)
            rightMax = hd

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    while left:
        res.append(left.pop())

    res.append(root.val)

    for node in right:
        res.append(node)

    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print(topView(root))