# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

# In the ith operation (1-indexed), you will:

    # Choose two elements, x and y.
    # Receive a score of i * gcd(x, y).
    # Remove x and y from nums.

# Return the maximum score you can receive after performing n operations.

# The function gcd(x, y) is the greatest common divisor of x and y.


from math import gcd

def maxScore(nums):

    memo = [-1] * (1 << len(nums))

    def DFS(mask, op):
        if memo[mask] != -1:
            return memo[mask]
        
        max_score = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                # If the numbers are same, or already picked, then we move to next number.
                if (mask >> i) & 1 == 1 or (mask >> j) & 1 == 1:
                    continue
                
                # Both numbers are marked as picked in this new mask.
                new_mask = mask | (1 << i) | (1 << j)

                curr_score = op * gcd(nums[i], nums[j])
                max_score = max(max_score, curr_score + DFS(new_mask, op + 1))
        
        memo[mask] = max_score

        return max_score

    return DFS(0, 1)


nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


print(maxScore(nums))