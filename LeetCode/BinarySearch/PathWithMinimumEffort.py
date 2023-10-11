from collections import deque

def minimumEffortPath(heights):
    n = len(heights)
    m = len(heights[0])

    def BFS(minEffort):
        queue = deque([(0, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            
            if r == n - 1 and c == m - 1:
                return True
            

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + i, c + j
                
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    curr_diff = abs(heights[nr][nc] - heights[r][c])
                    
                    if curr_diff <= minEffort:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
    
    left, right = 0, 10**6

    while left < right:
        mid = (left + right) // 2
        if BFS(mid):
            right = mid
        else:
            left = mid + 1
        
    return left


heights = [[1,2,3],
           [3,8,4],
           [5,3,5]]

print(minimumEffortPath(heights))