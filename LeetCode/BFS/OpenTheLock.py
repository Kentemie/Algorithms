# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of 
# turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop 
# turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns
# required to open the lock, or -1 if it is impossible.

from collections import deque

def createCombination(lock):
    for i in range(4):
        wheel = int(lock[i])
        for move in (-1, 1):
            new_wheel = (wheel + move) % 10
            yield lock[:i] + str(new_wheel) + lock[i+1:]
            
def BFS(deadends, target):
    queue = deque([('0000', 0)])
    deadends = set(deadends)
    seen = {'0000'}

    while queue:
        lock, lvl = queue.popleft()
        if lock == target:
            return lvl
        if lock in deadends:
            continue
        for combination in createCombination(lock):
            if combination not in seen:
                queue.append((combination, lvl + 1))
            seen.add(combination)
        
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print(BFS(deadends, target))