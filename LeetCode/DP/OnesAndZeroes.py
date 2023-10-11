# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

def findMaxForm(strs, m, n):
    dp = {}

    def DFS(i, m, n):
        if i == len(strs):
            return 0
        if (i, m, n) in dp:
            return dp[(i, m, n)]
        
        dp[(i, m, n)] = DFS(i + 1, m, n)

        mCnt, nCnt = strs[i].count("0"), strs[i].count("1")
        if mCnt <= m and nCnt <= n:
            # +1 means we including current string
            dp[(i, m, n)] = max(dp[(i, m, n)], 1 + DFS(i + 1, m - mCnt, n - nCnt))

        return dp[(i, m, n)]
    
    return DFS(0, m, n)

strs = ["10","0001","111001","1","0"]
m = 5
n = 3   

print(findMaxForm(strs, m, n))