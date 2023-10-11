# You are given an m x n grid rooms initialized with these three possible values.

    # -1 A wall or an obstacle.
    # 0 A gate.
    # INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance 
    # to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

from collections import deque

def wallsAndGates(rooms):
    queue = deque()
    
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))

    while queue:
        row, col, step = queue.popleft()
        for i, j in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if 0 <= row + i < len(rooms) and 0 <= col + j < len(rooms[0]):
                if rooms[row + i][col + j] == 2147483647:
                    rooms[row + i][col + j] = step + 1
                    queue.append((row + i, col + j, step + 1))

    return rooms


rooms = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]

res = wallsAndGates(rooms)

for row in res:
    print(row)