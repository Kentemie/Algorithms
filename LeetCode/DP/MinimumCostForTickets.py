# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer 
# array days. Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
#     a 1-day pass is sold for costs[0] dollars,
#     a 7-day pass is sold for costs[1] dollars, and
#     a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
#     For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

# def minCostTickets(day):
#     if day in memo:
#         return memo[day]
    
#     if day > 365:
#         return 0
#     elif day in dayset:
#         one_day_pass = minCostTickets(day + 1) + costs[0]
#         seven_days_pass = minCostTickets(day + 7) + costs[1]
#         thirty_days_pass = minCostTickets(day + 30) + costs[2]

#         memo[day] = min(one_day_pass, seven_days_pass, thirty_days_pass)
        
#         return memo[day]
#     else:
#         return minCostTickets(day + 1)


# days = [1,4,6,7,8,20]
# costs = [2,7,15]

# durations = [1,7,30]
# dayset = set(days)
# memo = {}

# print(minCostTickets(1))


def minCostTickets(i):
    if i in memo:
        return memo[i]

    if i >= n:
        return 0
    
    minCost = float('inf')
    j = i

    for c, d in zip(costs, durations):
        while j < n and days[j] < days[i] + d:
            j += 1
        minCost = min(minCost, minCostTickets(j) + c)
    memo[i] = minCost
    
    return minCost


days = [1,4,6,7,8,20]
costs = [2,7,15]

durations = [1,7,30]
n = len(days)
memo = {}

print(minCostTickets(0))


