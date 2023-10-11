# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position 
# where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is
# more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

def mostCompetitive(nums, k):
    stack = []
    cnt = len(nums) - k

    for num in nums:
        while stack and num < stack[-1] and cnt > 0:
            stack.pop()
            cnt -= 1  
        stack.append(num)

    return stack[:k]

nums = [3,5,2,6]
k = 2

# nums = [3,5,7,9,2,3]
# k = 3

# nums = [2,4,3,3,5,4,9,6]
# k = 4

print(mostCompetitive(nums, k))