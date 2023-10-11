# Construct inorder traversal by sorting the preorder array.

# Construct binary tree from preorder and inorder traversal:

# The idea is to peek the elements one by one from the preorder array and try to put them as a left or as a right child if 
# it's possible. If it's impossible - just put null as a child and proceed further. The possibility to use an element as a
# child is checked by an inorder array: if it contains no elements for this subtree, then the element couldn't be used here,
# and one should use null as a child instead.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder):
    inorder = sorted(preorder)
    idx_map = {val:idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    
    def DFS(in_left = 0, in_right = len(preorder)):
        nonlocal pre_idx
        if in_left == in_right:
            return None
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)

        idx = idx_map[root_val]
        pre_idx += 1

        root.left = DFS(in_left, idx)
        root.right = DFS(idx + 1, in_right)

        return root
    
    return DFS()