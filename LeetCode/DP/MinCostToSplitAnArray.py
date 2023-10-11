# You are given an integer array nums and an integer k.

# Split the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray 
# in the split.

# Let trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.

    # For example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].

# The importance value of a subarray is k + trimmed(subarray).length.

    # For example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray 
    # will be k + 5.

# Return the minimum possible cost of a split of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.


def minCost(nums, k):
    n = len(nums)
    dp = [-1] * n
    def DFS(i):
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]
        
        min_cost = float("inf")
        trimmed_len = 0
        counter = {}

        for j in range(i, n):
            counter[nums[j]] = counter.get(nums[j], 0) + 1

            if counter[nums[j]] == 2:
                trimmed_len += 2
            elif counter[nums[j]] > 2:
                trimmed_len += 1
            
            importance_value = k + trimmed_len

            if importance_value > min_cost:
                break

            min_cost = min(min_cost, importance_value + DFS(j + 1))

        dp[i] = min_cost
        return min_cost

    return DFS(0)

nums = [1,2,1,2,1,3,3]
k = 2
nums = [1,2,1,2,1]
k = 2
nums = [1,2,1,2,1]
k = 5
nums = [1,2,3,4,5]
k = 1

print(minCost(nums, k))