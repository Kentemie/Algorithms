# There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

    # Eat one orange.
    # If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
    # If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.

# You can only choose one of the actions per day.

# Given the integer n, return the minimum number of days to eat n oranges.

def minDays(n):
    dp = {0: 0, 1: 1}

    def DFS(n):
        if n in dp:
            return dp[n]
        
        divide_by_two = 1 + n % 2 + DFS(n // 2)
        divide_by_three = 1 + n % 3 + DFS(n // 3)

        dp[n] = min(divide_by_two, divide_by_three)
        return dp[n]

    return DFS(n)

n = 6

print(minDays(n))