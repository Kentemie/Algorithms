# You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You 
# are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel 
# you have, respectively.

# At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. 
# Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes 
# the absolute value of x.

# Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including 
# start and finish).

# Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.


def countRoutes(locations, start, finish, fuel):
    mod = (10 ** 9) + 7
    n = len(locations)
    dp = [[-1] * (fuel + 1) for _ in range(n)]

    def DFS(i, fuel_left):
        if fuel_left < 0:
            return 0
        if dp[i][fuel_left] != -1:
            return dp[i][fuel_left]
        
        dp[i][fuel_left] = 1 if i == finish else 0
        for j in range(n):
            if i == j:
                continue
            dp[i][fuel_left] += DFS(j, fuel_left - abs(locations[i] - locations[j])) % mod
        
        return dp[i][fuel_left] % mod
    
    return DFS(start, fuel)
        

locations = [2,3,6,8,4]
start = 1
finish = 3
fuel = 5

locations = [4,3,1]
start = 1
finish = 0
fuel = 6

print(countRoutes(locations, start, finish, fuel))