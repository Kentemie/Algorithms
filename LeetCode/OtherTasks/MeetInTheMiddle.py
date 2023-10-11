# Given a set of n integers where n <= 40. Each of them is at most 1012, determine the maximum sum subset having sum less 
# than or equal S where S <= 1018.

def search(arr, x):
    l, r = 0, len(arr)

    while l < r:
        mid = (r + l) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    
    return l

def calc(nums, arr, n, c):
    for i in range(1 << n):
        _sum = 0
        for j in range(n):
            if (i >> j) & 1:
                _sum += nums[j + c]
        arr[i] = _sum

def solve(nums, s):
    n = len(nums)
    nLeft = n // 2
    nRight = n - n // 2

    left = [0] * (1 << nLeft)
    right = [0] * (1 << nRight)

    calc(nums, left, nLeft, 0)
    calc(nums, right, nRight, n // 2)

    right.sort()
    max_possible = 0

    for i in range(nLeft):
        if left[i] <= s:
            pos = search(right, s - left[i])

            if pos == (1 << nRight) or right[pos] != s - left[i]:
                pos -= 1

            if left[i] + right[pos] > max_possible:
                max_possible = left[i] + right[pos]

    return max_possible

nums = [3,34,4,12,5,2]
s = 10

nums = [45,34,4,12,5,2]
s = 42

print(solve(nums, s))