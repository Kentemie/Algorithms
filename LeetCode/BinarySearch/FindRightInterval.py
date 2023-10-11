# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

def findRightInterval(intervals):
    starts = []

    for idx, interval in enumerate(intervals):
        starts.append([interval[0], idx])
    
    starts.sort(key = lambda x: x[0])

    def search(x):
        left, right = 0, len(starts)

        while left < right:
            mid = (left + right) // 2
            if starts[mid][0] < x:
                left = mid + 1
            else:
                right = mid

        return left

    res = []

    for _, end in intervals:
        idx = search(end)
        if idx != len(starts):
            res.append(starts[idx][1])
        else:
            res.append(-1)

    return res


intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.

intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

intervals = [[1,1],[3,4]]

print(findRightInterval(intervals))