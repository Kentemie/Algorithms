# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root, to_delete):
    to_delete = set(to_delete)
    res = []

    def DFS(node):
        if not node:
            return None

        node.left = DFS(node.left)
        node.right = DFS(node.right)

        if node.val in to_delete:
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            return None

        return node
    
    node = DFS(root)
    if node:
        res.append(node)
    
    return res


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
to_delete = [3,5]

print(delNodes(root, to_delete))