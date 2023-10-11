# You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the
# current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return
# the minimum time required for all buses to complete at least totalTrips trips.

def minimumTime(time, totalTrips):
    n = len(time)
    left = 1
    right = min(time) * totalTrips

    while left < right:
        mid = (right + left) // 2
        totalTime = 0
        for i in range(n):
            totalTime += mid // time[i]
        if totalTime >= totalTrips:
            right = mid
        else:
            left = mid + 1
    
    return right


time = [1,2,3]
totalTrips = 5

# time = [2]
# totalTrips = 1

print(minimumTime(time, totalTrips))