# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    def binarySearch(left, right):
        while left <= right:
            mid = (left + right) // 2
            midElem = matrix[mid // m][mid % m]
            if target == midElem:
                return True
            elif target > midElem:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    return binarySearch(0, n * m - 1)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(searchMatrix(matrix, target))