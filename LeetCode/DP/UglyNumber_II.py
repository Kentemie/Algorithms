# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

def nthUglyNumber(n):
    nums = [1]
    i2 = i3 = i5 = 0

    for _ in range(1, n):
        ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
        nums.append(ugly)

        if ugly == nums[i2] * 2:
            i2 += 1
        if ugly == nums[i3] * 3:
            i3 += 1
        if ugly == nums[i5] * 5:
            i5 += 1

    return nums[-1]

n = 11
print(nthUglyNumber(n))