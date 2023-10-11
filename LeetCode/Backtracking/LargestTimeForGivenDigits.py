# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 
# 24-hour time is 00:00, and the latest is 23:59.

# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

def largestTimeFromDigits(arr):
    max_time = -1

    def buildTime(arr):
        nonlocal max_time
        h, i, j, k = arr
        hour = h * 10 + i
        minute = j * 10 + k
        if hour < 24 and minute < 60:
            max_time = max(max_time, hour * 60 + minute)

    def swap(arr, i, j):
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]

    def permutate(arr, start):
        if start == len(arr):
            buildTime(arr)
            return 
        for i in range(start, len(arr)):
            swap(arr, i, start)
            permutate(arr, start + 1)
            swap(arr, i, start)

    permutate(arr, 0)

    if max_time == -1:
        return ""
    return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

arr = [1,2,3,4]
# arr = [5,5,5,5]

print(largestTimeFromDigits(arr))