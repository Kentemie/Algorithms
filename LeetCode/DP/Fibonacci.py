# Iterative Bottom-Up Approach

# Time complexity: O(N)O(N)O(N). Each value from 2 to N is computed once. Thus, the time it takes to find the answer is directly proportional 
# to N where N is the Fibonacci Number we are looking to compute.

# Space complexity: O(1)O(1)O(1). This requires 1 unit of space for the integer N and 3 units of space to store the computed values 
# (current, prev1, and prev2) for every loop iteration. The amount of space used is independent of NNN, so this approach uses a constant 
# amount of space.

def fib(n):
    if n <= 1:
        return n
    
    curr = 0
    prev1 = 1
    prev2 = 0

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return curr

print(fib(10))