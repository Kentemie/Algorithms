# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1)
# respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost    
# column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these 
# nodes by their values.

# Return the vertical order traversal of the binary tree.


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrderTraversal(root):
    if not root:
        return []
    
    verticalOrder = {}
    result = []
    start = end = 0 # range of the columns
    queue = deque([(root, 0, 0)]) # node, num of row, num of column

    while queue:
        node, row, col = queue.popleft()
        
        verticalOrder.setdefault(col, []).append((row, node.val))
        start = min(start, col)
        end = max(end, col)

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    for col in range(start, end + 1):
        result.append([val for _, val in sorted(verticalOrder[col])])

    return result 

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))

print(verticalOrderTraversal(root))