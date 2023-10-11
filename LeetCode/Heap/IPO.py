# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to
# work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct
# projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total
# capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.


from heapq import heapify, heappop, heappush

def findMaximizedCapital(k, w, profits, capital):
    max_profit = []
    min_capital = [(c, p) for c, p in zip(capital, profits)]
    heapify(min_capital)

    for _ in range(k):
        while min_capital and min_capital[0][0] <= w:
            _, p = heappop(min_capital)
            heappush(max_profit, -1 * p)
        if not max_profit:
            break
        w += -1 * heappop(max_profit)

    return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

print(findMaximizedCapital(k, w, profits, capital))