# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in
# a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another
# computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be 
# deserialized to the original tree structure.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Conversion:

    def serialize2(self, root):
        if not root:
            return "None "
        left = self.serialize2(root.left)
        right = self.serialize2(root.right)
        return str(root.val) + " " + left + right
    
    def serialize(self, root):
        if not root:
            return 'N'

        queue = deque([root])
        data = []

        while queue:
            node = queue.popleft()
            
            if node:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append('N')

        j = len(data) - 1

        while True:
            if data[j] != 'N':
                break
            j -= 1

        return ",".join(data[:j + 1])
    
    def deserialize(self, data):
        if not data:
            return None

        nodes = deque(data.split(","))
        root_val = nodes.popleft()
        if root_val == 'N':
            return None

        root = TreeNode(int(root_val))
        queue = deque([root])

        while queue and nodes:
            node = queue.popleft()
            left_val = nodes.popleft() if nodes else 'N'
            right_val = nodes.popleft() if nodes else 'N'

            if left_val != 'N':
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            
            if right_val != 'N':
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

        return root
    
codec = Conversion()

data = ['4','-7','-3','N','N','-9','-3','9','-7','-4','N','6','N','-6','-6','N','N','0','6','5','N','9','N','N','-1','-4',
        'N','N','N','-2']

data = ",".join(data)

node = codec.deserialize(data)

data = codec.serialize(node)
data2 = codec.serialize2(node)

print(len(data.split(',')))
print(len(data2.split(' ')))