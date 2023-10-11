# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
# postorder is the postorder traversal of the same tree, construct and return the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    idxMap = {val:idx for idx, val in enumerate(inorder)}
    def DFS(in_left = 0, in_right = len(postorder)):   
        if in_left == in_right:
            return None
        root_val = postorder.pop()

        root = TreeNode(root_val)
        index = idxMap[root_val]
        
        root.right = DFS(index + 1, in_right)
        root.left = DFS(in_left, index)

        return root
    
    return DFS()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]