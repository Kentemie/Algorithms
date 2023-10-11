# You are given two integers m and n that represent the height and width of a rectangular piece of wood. You are also given a 2D 
# integer array prices, where prices[i] = [hi, wi, pricei] indicates you can sell a rectangular piece of wood of height hi and 
# width wi for pricei dollars.

# To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it 
# into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to prices. 
# You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you cannot rotate a piece to swap its height and width.

# Return the maximum money you can earn after cutting an m x n piece of wood.

# Note that you can cut the piece of wood as many times as you want.

def sellingWood(m, n, prices):
    price_map = {}

    for height, width, price in prices:
        if height in price_map:
            price_map[height][width] = price
        else:
            price_map[height] = { width: price }

    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    def get_price(height, width):
        if height in price_map and width in price_map[height]:
            return price_map[height][width]
        return 0
    
    def DFS(height, width):
        if dp[height][width] != -1:
            return dp[height][width]
        
        price = get_price(height, width)

        for i in range(1, height):
            price = max(price, DFS(i, width) + DFS(height - i, width))

        for j in range(1, width):
            price = max(price, DFS(height, j) + DFS(height, width - j))

        dp[height][width] = price

        return price
    
    return DFS(m, n)

m = 3
n = 5
prices = [[1,4,2],[2,2,7],[2,1,3]]

m = 4
n = 6
prices = [[3,2,10],[1,4,2],[4,1,3]]

print(sellingWood(m, n, prices))