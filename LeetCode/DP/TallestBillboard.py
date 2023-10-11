# You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side.
# Each steel support must be an equal height.

# You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld
#  them together to make a support of length 6.

# Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

def tallestBillboard(rods):
    n = len(rods)
    memo = {}

    def DFS(i, diff):
        if i == n:
            return 0 if diff == 0 else float("-inf")
        
        if (i, diff) in memo:
            return memo[(i, diff)]

        op1 = rods[i] + DFS(i + 1, diff + rods[i])
        op2 = DFS(i + 1, diff - rods[i])
        op3 = DFS(i + 1, diff)

        memo[(i, diff)] = max(op1, op2, op3)
        
        return memo[(i, diff)]
    
    return DFS(0, 0)

rods = [1,2,3,4,5,6]
rods = [1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]

print(tallestBillboard(rods))