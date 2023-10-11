# Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

# If there is no way to make arr1 strictly increasing, return -1.

def makeArrayIncreasing(arr1, arr2):
    arr2.sort()
    dp = {}

    def search(x):
        left = 0
        right = len(arr2)

        while left < right:
            mid = (right + left) // 2
            if x < arr2[mid]:
                right = mid
            else:
                left = mid + 1
        
        return left

    def DFS(i, prev):
        if i == len(arr1):
            return 0
        if (i, prev) in dp:
            return dp[(i, prev)]
        
        res = float("inf")
        if prev < arr1[i]:
            res = DFS(i + 1, arr1[i])

        j = search(prev)
        if j < len(arr2):
            res = min(res, 1 + DFS(i + 1, arr2[j]))

        dp[(i, prev)] = res
        return res
    
    res = DFS(0, -1)
    return res if res != float("inf") else -1

        
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]

arr1 = [1,5,3,6,7]
arr2 = [4,3,1]

arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]

print(makeArrayIncreasing(arr1, arr2))