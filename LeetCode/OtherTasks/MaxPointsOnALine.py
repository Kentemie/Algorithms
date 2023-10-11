# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of
# points that lie on the same straight line.


def maxPoints(points):
    n = len(points)

    if n == 1:
        return 1
    
    def findLine(x0, y0, x1, y1):
        if x0 == x1:
            return (x0, None) # slope is x0 because y never changes and there is no intercept with y-axis
        if y0 == y1:
            return (0, y0) # slope is 0 because x never changes and intercept is with y-axis is y0
        
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        return (slope, intercept)
    
    lines = {}

    for i in range(n):
        for j in range(i + 1, n):
            line = findLine(points[i][0], points[i][1], points[j][0], points[j][1])
            lines.setdefault(line, set()).add(i)
            lines.setdefault(line, set()).add(j)

    return max(len(lines[line]) for line in lines)


def maxPoints1(points):
    n = len(points)
    res = 1
    for i in range(n - 1):
        x0, y0 = points[i]
        counter = {}
        for j in range(i + 1, n):
            x1, y1 = points[j]

            if x0 == x1:
                slope = float("inf")
            else:
                slope = (y1 - y0) / (x1 - x0)
            
            counter[slope] = counter.get(slope, 0) + 1
            res = max(res, counter[slope] + 1)
        
    return res


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

print(maxPoints(points))
print(maxPoints1(points))