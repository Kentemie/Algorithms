# An Integral image is where each pixel represents the cumulative sum of a corresponding input pixel with all pixels above
#  and left of the input pixel. It enables rapid calculation of summations over image sub-regions. Any rectangular subset 
#  of such sub-region can be evaluated in constant time.

# This concept was introduced by Viola & Jones and is also known as Summed Area Table. allow fast computation of 
# rectangular image features since they enable the summation of image values over any rectangle image region in constant
# time i.e. computational complexity of O(1) instead of O(n).

# An Integral Image is defined as:

    # S(x,y) = I(x, y) + S(x - 1, y) + S(x, y - 1) - S(x - 1, y - 1)

# The SAT method has

    # Space Complexity: O(M*N)
    # Time Complexity for Range Sum Query: O(1)
    # Time Complexity to Update a Value in Matrix: O(M*N)
    # Efficiently computes the statistics like mean, standard deviation, etc in any rectangular window

def integralImage(image):
    n = len(image)
    m = len(image[0])
    SAT = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            SAT[i][j] = image[i - 1][j - 1] + SAT[i - 1][j] + SAT[i][j - 1] - SAT[i - 1][j - 1]
    
    return SAT

def sumRegion(row1, col1, row2, col2):
    return SAT[row2 + 1][col2 + 1] - (SAT[row2 + 1][col1] + SAT[row1][col2 + 1] - SAT[row1][col1])

image = [[4,5,2,1], 
         [0,9,3,2], 
         [5,6,8,1], 
         [2,3,0,0]]

SAT = integralImage(image)

print(sumRegion(1,1,2,3))