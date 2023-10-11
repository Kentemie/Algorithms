# You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. 
# Each steel support must be an equal height.

# You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld 
# them together to make a support of length 6.

# Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.


def helper(half_rods):
    states = { (0, 0) }

    for rod in half_rods:
        new_states = set()
        for left, right in states:
            new_states.add((left + rod, right))
            new_states.add((left, right + rod))
        states |= new_states
    
    dp = {}

    for left, right in states:
        dp[left - right] = max(dp.get(left - right, 0), left)
    
    return dp

def tallestBillboard(rods):
    n = len(rods) // 2
    left_half = helper(rods[:n])
    right_half = helper(rods[n:])
    res = 0

    for diff in left_half:
        if -diff in right_half:
            res = max(res, left_half[diff] + right_half[-diff])
    
    return res

rods = [1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]

print(tallestBillboard(rods))