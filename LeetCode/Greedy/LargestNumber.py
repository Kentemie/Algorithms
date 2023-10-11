# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key

def compare(n1, n2):
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1

def largestNumber(nums):
    largest_num = "".join(sorted(map(str, nums), key = cmp_to_key(compare)))
    return largest_num if largest_num[0] != "0" else "0"

nums = [10,2]
"210"

nums = [3,30,34,5,9]
# "9534330"

print(largestNumber(nums))