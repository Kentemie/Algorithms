# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n
# nodes of unique values from 1 to n.

def numTrees(n):
    # numTrees[4] = numTrees[0] * numTrees[3] +
                #   numTrees[1] * numTrees[2] +
                #   numTrees[2] * numTrees[1] +
                #   numTrees[3] * numTrees[0] 
    numTree = [1] * (n + 1)
    
    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += numTree[left] * numTree[right]
        numTree[nodes] = total
    
    return numTree[n]

print(numTrees(6))