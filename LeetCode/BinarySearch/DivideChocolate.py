# You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

# You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k 
# cuts, each piece consists of some consecutive chunks.

# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

def maximizeSweetness(sweetness, k):
    left = min(sweetness)
    right = sum(sweetness) // (k + 1)

    while left < right:
        mid = (left + right + 1) // 2
        currSweetness = 0
        peopleWithPiece = 0
        for s in sweetness:
            currSweetness += s
            if currSweetness >= mid:
                peopleWithPiece += 1
                currSweetness = 0
        if peopleWithPiece >= k + 1:
            left = mid
        else:
            right = mid - 1

    return right

sweetness = [1,2,3,4,5,6,7,8,9]
k = 5
# 6

sweetness = [5,6,7,8,9,1,2,3,4]
k = 8
# 1

sweetness = [1,2,2,1,2,2,1,2,2]
k = 2
# 5

print(maximizeSweetness(sweetness, k))