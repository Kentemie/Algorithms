# You are given a floating-point number hour, representing the amount of time you have to reach the office. To
# commute to the office, you must take n trains in sequential order. You are also given an integer array dist of
# length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may need to wait in between each train ride.

    # For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can 
    # depart on the 2nd train ride at the 2 hour mark.

# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you
# to reach the office on time, or -1 if it is impossible to be on time.

# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

from math import ceil

def minSpeedOnTime(dist, hour):
    n = len(dist)
    res = float('inf')
    left = 1
    right = 10**9 - 7

    while left <= right:
        speed = (left + right) // 2
        totalTime = 0

        for i in range(n - 1):
            totalTime += ceil(dist[i] / speed)
        totalTime += dist[-1] / speed

        if totalTime <= hour:
            res = min(res, speed)
            right = speed - 1
        else:
            left = speed + 1

    return res if res != float('inf') else -1


dist = [1,3,2]
hour = 6

dist = [1,3,2]
hour = 2.7

dist = [1,3,2]
hour = 1.9

dist = [1,1,100000]
hour = 2.01

print(minSpeedOnTime(dist, hour))