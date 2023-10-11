# Given an integer n, return the least number of perfect square numbers that sum to n.

def BFS(n):
    squareNums = [i * i for i in range(1, int(n ** 0.5) + 1)]
    lvl = 0
    queue = {n}

    while queue:
        lvl += 1
        nextQueue = set()

        for remainder in queue:
            for squareNum in squareNums:
                if remainder == squareNum:
                    return lvl 
                elif remainder < squareNum:
                    break
                else:
                    nextQueue.add(remainder - squareNum)
        
        queue = nextQueue
    
    return lvl

n = 12
# 3

print(BFS(n))