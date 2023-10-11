def canReach(arr, start):
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        arr[start] = -arr[start]
        return canReach(arr, start + arr[start]) or canReach(arr, start - arr[start])
    return False


arr = [4,2,3,0,3,1,2]
start = 5

print(canReach(arr, start))