from collections import deque 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def levelOrder(root):
    res = []
    
    if not root:
        return res
    
    queue = deque([root])

    while queue:
        lvl = []
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            lvl.append(node.val)
            queue.extend(node.children)
        res.append(lvl)

    return res

