# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.

from heapq import heappop, heappush

def maxEvents(events):
    events.sort()
    numOfAttend = []
    cnt = i = 0
    currDay = events[0][0]
    while i < len(events):
        while i < len(events) and events[i][0] == currDay:
            heappush(numOfAttend, events[i][1])
            i += 1
        heappop(numOfAttend)
        cnt += 1
        currDay += 1
        while numOfAttend and numOfAttend[0] < currDay:
            heappop(numOfAttend)
        if i < len(events) and not numOfAttend:
            currDay = events[i][0]

    while numOfAttend:
        if heappop(numOfAttend) >=currDay:
            cnt += 1
            currDay += 1
    
    return cnt

events = [[1,2],[2,3],[3,4]]
# events= [[1,2],[2,3],[3,4],[1,2]]
# events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# events = [[1,2],[2,2],[3,3],[3,4],[3,4]]
print(maxEvents(events))