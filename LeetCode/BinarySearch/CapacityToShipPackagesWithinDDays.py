# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor
# belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped 
# within days days.

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        daysNeeded = 1
        currWeight = 0
        for weight in weights:
            currWeight += weight
            if currWeight > mid:
                daysNeeded += 1
                currWeight = weight

        if daysNeeded <= days:
            right = mid
        else:
            left = mid + 1
    
    return right

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
# 15

weights = [3,2,2,4,1,4]
days = 3
# 6

weights = [1,2,3,1,1]
days = 4
# 3

print(shipWithinDays(weights, days))