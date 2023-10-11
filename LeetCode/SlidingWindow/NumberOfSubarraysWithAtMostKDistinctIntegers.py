def numOfDistinctSubarrays(nums, k):
    frequency = {}
    left = 0 
    distinctCnt = 0
    cnt = 0

    for right in range(len(nums)):
        frequency[nums[right]] = frequency.get(nums[right], 0) + 1
        if frequency[nums[right]] == 1:
            distinctCnt += 1
        while distinctCnt > k:
            frequency[nums[left]] -= 1
            if frequency[nums[left]] == 0:
                distinctCnt -= 1
            left += 1
        cnt += right - left + 1

    return cnt


nums = [1,2,1,2,3]
k = 2

print(numOfDistinctSubarrays(nums, k))