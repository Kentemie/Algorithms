from collections import deque

def maxSlidingWindow(nums, k):
    n = len(nums)

    if n * k == 0:
        return []
    if k == 1:
        return nums
    
    def clean(i):
        if queue and queue[0] == i - k:
            queue.popleft()
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

    queue = deque()
    max_idx = 0
    for i in range(k):
        clean(i)
        queue.append(i)

        print(queue)

        if nums[i] > nums[max_idx]:
            max_idx = i
    print()
    result = [nums[max_idx]]

    for i in range(k, n):
        clean(i)
        queue.append(i)

        print(queue)

        result.append(nums[queue[0]])

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums = [10,-2,-10,-5,20]
k = 2

nums = [-1000,-2000,-3000,-4000,2]
k = 2

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

print(maxSlidingWindow(nums, k))