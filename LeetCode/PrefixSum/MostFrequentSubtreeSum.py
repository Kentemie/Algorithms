# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with
# the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node 
# (including the node itself).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findFrequentTreeSum(root):
    global k
    if not root:
        return 0
    
    left_sub_tree = findFrequentTreeSum(root.left)
    right_sub_tree = findFrequentTreeSum(root.right)
    currSum = root.val + left_sub_tree + right_sub_tree
    subTreeSum[currSum] = subTreeSum.get(currSum, 0) + 1
    k = max(k, subTreeSum[currSum])

    return currSum
    
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)

k = 0
subTreeSum = {}
res = []

findFrequentTreeSum(root)

for prefSum in subTreeSum:
    if subTreeSum[prefSum] == k:
        res.append(prefSum)

print(res)