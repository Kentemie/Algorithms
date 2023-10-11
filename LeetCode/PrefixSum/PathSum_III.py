# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along 
# the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent 
# nodes to child nodes).


"""
You might want to use the prefix sum technique for the problems like 'Find a number of continuous subarrays/submatrices/
tree paths that sum to target'.
"""


from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum) -> int:
        def preOrder(root, currSum):
            nonlocal cnt
            if not root:
                return
            currSum += root.val
            if currSum == targetSum:
                cnt += 1
            cnt += hashmap[currSum - targetSum]
            hashmap[currSum] += 1
            preOrder(root.left, currSum)
            preOrder(root.right, currSum)
            hashmap[currSum] -= 1
            
        cnt = 0
        hashmap = defaultdict(int)
        preOrder(root, 0)
        return cnt

