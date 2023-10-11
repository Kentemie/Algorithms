# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

def largestRectangleArea(heights):
    stack = [-1]
    maxArea = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        maxArea = max(maxArea, height * width)

    return maxArea


heights = [2,1,5,6,2,3]
heights = [2,4]

print(largestRectangleArea(heights))