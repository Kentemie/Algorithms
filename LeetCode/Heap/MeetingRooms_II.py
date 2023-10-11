# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of 
# conference rooms required.

from heapq import heappop, heappush

def minMeetingRooms(intervals):
    freeRooms = []
    intervals.sort(key = lambda x: x[0])
    heappush(freeRooms, intervals[0][1])

    for meeting in intervals[1:]:
        if freeRooms[0] <= meeting[0]:
            heappop(freeRooms)
        heappush(freeRooms, meeting[1])
    
    return len(freeRooms)

intervals = [[0,30],[5,20],[15,20]]
# 3
intervals = [[0,30],[5,10],[15,20]]
# 2
intervals = [[7,10],[2,4]]
# 1

print(minMeetingRooms(intervals))