# You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer 
# array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

# The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed 
# of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

# You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge.
# The weapon is fully charged at the very start.

# You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, 
# it counts as a loss, and the game ends before you can use your weapon.

# Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters 
# before they reach the city.

def countSort(arrivalTimes):
    k = max(arrivalTimes)
    countArr = [0] * (k + 1)
    outputArr = [0] * len(arrivalTimes)
    for time in arrivalTimes:
        countArr[time] += 1

    startingIndex = 0
    for i, cnt in enumerate(countArr):
        countArr[i] = startingIndex
        startingIndex += cnt 

    for time in arrivalTimes:
        outputArr[countArr[time]] = time
        countArr[time] += 1

    for i in range(len(arrivalTimes)):
        arrivalTimes[i] = outputArr[i]

def eliminateMaximum(dist, speed):
    n = len(dist)
    arrivalTimes = []

    for i in range(n):
        if dist[i] <= speed[i]:
            arrivalTimes.append(1)
        else:
            t = dist[i] // speed[i] + int(dist[i] % speed[i] != 0)
            arrivalTimes.append(t)
            
    countSort(arrivalTimes)    
    total = 0

    for i in range(1, n + 1):
        if arrivalTimes[i - 1] - i < 0:
            return total
        total += 1

    return total

dist = [1,3,4]
speed = [1,1,1]
# 3

dist = [3,2,4]
speed = [1,1,2]
# 3

dist = [1,2,2,3]
speed = [1,1,1,1]
# 2

dist = [3,2,4]
speed = [5,3,2]
# 1

dist = [3,3,9,8,4,2]
speed = [1,1,1,3,1,1]
# 3

print(eliminateMaximum(dist, speed))