# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
# of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = [intervals[0]]
    
    for interval in intervals[1:]:
        n = len(res)
        if interval[0] <= res[n - 1][1]:
            res[n - 1][1] = max(interval[1], res[n - 1][1])
        else:
            res.append(interval)
    
    return res

intervals = [[1,3],[2,6],[6,10],[15,18]]
# intervals = [[1,4],[4,5]]

print(merge(intervals))