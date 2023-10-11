# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the 
# earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time 
# slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

from heapq import heapify, heappop

def minAvailableDuration(slots1, slots2, duration):
    timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
    heapify(timeslots)

    while len(timeslots) > 1:
        _, end1 = heappop(timeslots)
        start2, _ = timeslots[0]
        if end1 >= start2 + duration:
            return [start2, start2 + duration]
    return []

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12

slots1 = [[0,2]]
slots2 = [[1,3]]
duration = 1

print(minAvailableDuration(slots1, slots2, duration))