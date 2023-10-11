def trap(height):
    stack = [-1]
    ans = i = 0
    while i < len(height):
        while stack[-1] != -1 and height[i] > height[stack[-1]]:
            top = stack.pop()
            if stack[-1] == -1:
                break
            ans += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])
        stack.append(i)
        i += 1

    return ans

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

print(trap(height))