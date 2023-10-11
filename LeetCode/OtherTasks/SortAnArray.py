# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smalles
# space complexity possible.

def merge(arr, L, M, R):
    left, right = arr[L:M + 1], arr[M + 1:R + 1]

    i, j, k = L, 0, 0
    
    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1
    
    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1
    
    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1

def mergeSort(arr, l, r):
    if l == r:
        return arr
    
    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)

    return arr

# -------------------------------------------------- #

def countSort(arr):
    max_val, min_val = max(arr), min(arr)
    range_of_vals = max_val - min_val + 1
    count_arr = [0] * range_of_vals
    output_arr = [0] * len(arr)

    for num in arr:
        count_arr[num - min_val] += 1

    starting_index = 0

    for i, cnt in enumerate(count_arr):
        count_arr[i] = starting_index
        starting_index += cnt

    for num in arr:
        output_arr[count_arr[num - min_val]] = num
        count_arr[num - min_val] += 1
    
    return output_arr

nums = [5,2,3,1]

print(mergeSort(nums, 0, len(nums) - 1))
print(countSort(nums))

# -------------------------------------------------- #

def calcMinRun(n):
    r = 0
    while n >= 64:
        print(n, r)
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(nums, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and nums[j] < nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

def merge(nums, left, mid, right):
    n1, n2 = mid - left + 1, right - mid
    leftSide, rightSide = [], []

    for i in range(n1):
        leftSide.append(nums[i + left])
    for j in range(n2):
        rightSide.append(j + 1 + mid)

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if leftSide[i] <= rightSide[j]:
            nums[k] = leftSide[i]
            i += 1
        else:
            nums[k] = rightSide[j]
            j += 1
        k += 1

    while i < n1:
        nums[k] = leftSide[i]
        i += 1
        k += 1
    
    while j < n2:
        nums[k] = rightSide[j]
        j += 1
        k += 1
 
def timSort(nums):
    n = len(nums)
    minRun = calcMinRun(n)

    for left in range(0, n, minRun):
        right = min(left + minRun - 1, n - 1)
        insertionSort(nums, left, right)
    
    run = minRun

    while run < n:

        for left in range(0, n, 2 * run):
            mid = min(left + run - 1, n - 1)
            right = min(left + 2 * run - 1, n - 1)
            if mid < right:
                merge(nums, left, mid, right)

        run *= 2


nums = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]


timSort(nums)

print(nums)