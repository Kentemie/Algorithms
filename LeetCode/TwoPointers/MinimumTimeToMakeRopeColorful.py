# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for 
# help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime 
# where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

def minCost(colors, neededTime):
    totalTime = longestTime = 0
    for i in range(len(colors)):
        if i > 0 and colors[i] != colors[i - 1]:
            longestTime = 0
        
        if longestTime > neededTime[i]:
            totalTime += neededTime[i]
        else:
            totalTime += longestTime
            longestTime = neededTime[i]
    return totalTime

colors = "abaac"
neededTime = [1,2,3,4,5]
# 3
colors = "aabaa"
neededTime = [1,2,3,4,1]
# 2

print(minCost(colors, neededTime))