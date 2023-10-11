# In computer science, a Segment Tree, also known as a statistic tree, is a tree data structure used for storing information
# about intervals, or segments. It allows querying which of the stored segments contain a given point. It is, in principle,
# a static structure; that is, it’s a structure that cannot be modified once it’s built. A similar data structure is the 
# interval tree.

from math import ceil, log2

class SegmentTree:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.height = ceil(log2(self.n)) + 1
        self.max_size = 2**self.height - 1
        self.segment_tree = [0] * self.max_size

        self.construct(0, len(nums) - 1, 0)

    def construct(self, left, right, tree_idx):
        if left == right:
            self.segment_tree[tree_idx] = self.nums[left]
            return 

        mid = (left + right) // 2
        self.construct(left, mid, tree_idx * 2 + 1)
        self.construct(mid + 1, right, tree_idx * 2 + 2)

        self.segment_tree[tree_idx] = self.segment_tree[tree_idx * 2 + 1] + self.segment_tree[tree_idx * 2 + 2]

    def sumRange(self, left, right):
        if left < 0 or right > self.n - 1 or left > right:
            return -1
        return self.getSum(0, self.n - 1, left, right, 0)
    
    def getSum(self, left, right, qleft, qright, tree_idx):
        # If segment of this node is a part of given range,
        # then return the sum of the segment
        if qleft <= left and qright >= right:
            return self.segment_tree[tree_idx]
        
        # If segment of this node is
        # outside the given range
        if right < qleft or left > qright:
            return 0
        
        mid = (left + right) // 2
        return self.getSum(left, mid, qleft, qright, tree_idx * 2 + 1) + self.getSum(mid + 1, right, qleft, qright, tree_idx * 2 + 2)
    
    def update(self, index, val):
        if index < 0 or index > self.n - 1:
            return -1
        
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateValue(0, self.n - 1, index, diff, 0)
    
    def updateValue(self, left, right, idx, diff, tree_idx):
        # Base Case: If the input index lies
        # outside the range of this segment
        if idx < left or idx > right:
            return 
        
        # If the input index is in range of this node,
        # then update the value of the node and its children
        self.segment_tree[tree_idx] += diff
        if left != right:
            mid = (left + right) // 2
            self.updateValue(left, mid, idx, diff, tree_idx * 2 + 1)
            self.updateValue(mid + 1, right, idx, diff, tree_idx * 2 + 2)


nums = [1, 3, 5, 7, 9, 11]

ST = SegmentTree(nums)

print(ST.segment_tree)
print(ceil(log2(6)))
# print(ST.sumRange(0, 2))
# ST.update(1, 2)
# print(ST.segment_tree)
# print(ST.sumRange(0, 2))