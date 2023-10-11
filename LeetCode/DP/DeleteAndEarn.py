# from collections import defaultdict
# from functools import cache

# nums = [1,1,1,2,4,5,5,5,6]

# points = defaultdict(int)
# maxNum = 0

# for num in nums:
#     points[num] += num 
#     maxNum = max(maxNum, num)

# @cache
# def maxPoints(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return points[num]
#     return max(maxPoints(num - 1), maxPoints(num - 2) + points[num])   

# print(maxPoints(maxNum))


from collections import defaultdict

nums = [2,2,3,3,3,4]

points = defaultdict(int)
maxNum = 0

for num in nums:
    points[num] += num
    maxNum = max(maxNum, num)

max_points = [0] * (maxNum + 1)
max_points[1] = points[1]

for num in range(2, len(max_points)):
    max_points[num] = max(points[num] + max_points[num-2], max_points[num-1])

print(max_points[-1])