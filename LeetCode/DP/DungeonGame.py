# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of
# m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his 
# way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 
# or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering 
# these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's 
# health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room 
# where the princess is imprisoned.

def calculateMinimumHP(dungeon):
    n = len(dungeon)
    m = len(dungeon[0])
    dp = [[0] * m for _ in range(n)]
    dp[-1][-1] = dungeon[-1][-1]
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if i == n - 1 and j != m - 1:
                dp[i][j] = min(0, dungeon[i][j] + dp[i][j + 1])
            elif i != n - 1 and j == m - 1:
                dp[i][j] = min(0, dungeon[i][j] + dp[i + 1][j])
            elif i != n - 1 and j != m - 1:
                dp[i][j] = min(0, max(dp[i + 1][j], dp[i][j + 1]) + dungeon[i][j])
            else:
                dp[i][j] = min(0, dungeon[i][j])

    return -dp[0][0] + 1



dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# 7
dungeon = [[0]]
# 1
dungeon = [[100]]
# 1

print(calculateMinimumHP(dungeon))