# You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water 
# supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

# If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or 
# both buckets by the end.

# Operations allowed:

    # Fill any of the jugs with water.
    # Empty any of the jugs.
    # Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

from collections import deque

def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    x, y, z = jug1Capacity, jug2Capacity, jug1Capacity + jug2Capacity

    steps = [-x, x, -y, y]

    queue = deque([0])
    visited = [0] * (z + 1)
    visited[0] = 1
    while queue:
        node = queue.popleft()
        if node == targetCapacity:
            return True
        for i in range(4):
            newNode = node + steps[i]
            if newNode >= 0 and newNode <= z and not visited[newNode]:
                queue.append(newNode)
                visited[newNode] = 1

    return False 

jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4

print(canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))



# # Using GCD

# def GCD(a, b):
#     if a == 0:
#         return b
#     return GCD(b % a, a)

# if jug1Capacity + jug2Capacity > targetCapacity:
#     print(targetCapacity % GCD(jug1Capacity, jug2Capacity) == 0)