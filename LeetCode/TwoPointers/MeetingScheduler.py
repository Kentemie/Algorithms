# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the 
# earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time 
# slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

def minAvailableDuration(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()
    ptr1 = ptr2 = 0
    while ptr1 < len(slots1) and ptr2 < len(slots2):
        intersect_right = min(slots1[ptr1][1], slots2[ptr2][1])
        intersect_left = max(slots1[ptr1][0], slots2[ptr2][0])
        if intersect_right - intersect_left >= duration:
            return [intersect_left, intersect_left + duration]
        if slots1[ptr1][1] > slots2[ptr2][1]:
            ptr2 += 1
        else:
            ptr1 += 1
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