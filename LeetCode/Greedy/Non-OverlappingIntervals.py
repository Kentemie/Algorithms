# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you 
# need to remove to make the rest of the intervals non-overlapping.

def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    cnt = 0
    k = float('-inf')
    for start, end in intervals:
        if start >= k:
            k = end
        else:
            cnt += 1
    return cnt

intervals = [[1,5],[2,3],[4,5],[5,6]]

# intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]

print(eraseOverlapIntervals(intervals))