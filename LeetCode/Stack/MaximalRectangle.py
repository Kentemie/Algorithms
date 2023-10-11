# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

def maxArea(heights):
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i) 

    while stack[-1] != -1:
        max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))

    return max_area

def maximalRectangle(matrix):
    dp = [0] * len(matrix[0])
    maxRect = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            dp[col] = dp[col] + 1 if matrix[row][col] == '1' else 0
        maxRect = max(maxRect, maxArea(dp))

    return maxRect        

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

print(maximalRectangle(matrix))