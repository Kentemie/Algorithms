# Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree
# (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums 
# so that the constructed BST is identical to that formed from the original array nums.

    # For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] 
    # also yields the same BST but [3,2,1] yields a different BST.

# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

# Since the answer may be very large, return it modulo 10^9 + 7.

def numOfWays(nums):
    mod = (10 ** 9) + 7
    n = len(nums)
    Pascals_Triangle = []

    for i in range(n + 1):
        row = [0] * (i + 1)
        row[0] = row[-1] = 1

        for j in range(1, len(row) - 1):
            row[j] = (Pascals_Triangle[i - 1][j - 1] + Pascals_Triangle[i - 1][j]) % mod

        Pascals_Triangle.append(row)

    def DFS(nums):
        m = len(nums)
        if m <= 2:
            return 1
        
        left_subtree, right_subtree = [], []
        for i in range(1, m):
            if nums[i] < nums[0]:
                left_subtree.append(nums[i])
            else:
                right_subtree.append(nums[i])

        left_ans = DFS(left_subtree)
        right_ans = DFS(right_subtree)

        return (left_ans * right_ans * Pascals_Triangle[m - 1][len(left_subtree)]) % mod
    
    return (DFS(nums) - 1) % mod

nums = [2,1,3]
# Output: 1
# Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums
# which will yield the same BST.

nums = [3,4,5,1,2]
# Output: 5
# Explanation: The following 5 arrays will yield the same BST: 
# [3,1,2,4,5]
# [3,1,4,2,5]
# [3,1,4,5,2]
# [3,4,1,2,5]
# [3,4,1,5,2]

nums = [1,2,3]
# Output: 0
# Explanation: There are no other orderings of nums that will yield the same BST.

print(numOfWays(nums))