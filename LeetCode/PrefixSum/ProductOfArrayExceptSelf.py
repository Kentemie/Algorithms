# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of 
# nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# For any nums[i], calculate its left product and calculate its right product, without including nums[i].
# Then multiply these left and right product, This will give product of array excluding nums[i].

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    suffProd = 1
    for i in reversed(range(n - 1)):
        suffProd *= nums[i + 1]
        res[i] *= suffProd

    return res

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

print(productExceptSelf(nums))