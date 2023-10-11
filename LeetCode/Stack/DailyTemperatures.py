# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the 
# number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which 
# this is possible, keep answer[i] == 0 instead.

temperatures = [73,74,75,71,69,72,76,73]

days = [0] * len(temperatures)
stack = [len(temperatures) - 1]

for i in reversed(range(len(temperatures) - 1)):
    while stack and temperatures[stack[-1]] <= temperatures[i]:
        stack.pop()
    if stack:
        days[i] = stack[-1] - i
    stack.append(i)

print(days)