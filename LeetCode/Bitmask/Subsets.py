def subsets(nums):
    n = len(nums)
    res = []

    for i in range(1 << n, 1 << (n + 1)): # 1 << n -> 2 ** n
        bitmask = bin(i)[3:]
        res.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return res

nums = [1,2,3]

print(subsets(nums))