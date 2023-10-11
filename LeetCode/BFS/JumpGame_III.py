# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at 
# index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

def canReach(arr, start):
    queue = [start]
    n = len(arr)

    while queue: 
        pos = queue.pop()
        if arr[pos] == 0:
            return True
        if arr[pos] < 0:
            continue
        for i in [pos + arr[pos], pos - arr[pos]]:
            if 0 <= i < n:
                queue.append(i)
        arr[pos] = -arr[pos]
    return False

# arr = [4,2,3,0,3,1,2]
# start = 5
# arr = [4,2,3,0,3,1,2]
# start = 0
# arr = [3,0,2,1,2]
# start = 2
arr = [0,3,0,6,3,3,4]
start = 6

print(canReach(arr, start))

# All possible ways to reach at index 3 with value 0 are: 
#   index 5 -> index 4 -> index 1 -> index 3 
#   index 5 -> index 6 -> index 4 -> index 1 -> index 3 