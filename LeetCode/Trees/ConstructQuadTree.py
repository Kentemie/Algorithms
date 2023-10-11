# Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

# Return the root of the Quad-Tree representing grid.

# A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    # val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
    # isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
    # class Node {
    #     public boolean val;
    #     public boolean isLeaf;
    #     public Node topLeft;
    #     public Node topRight;
    #     public Node bottomLeft;
    #     public Node bottomRight;
    # }

# We can construct a Quad-Tree from a two-dimensional area using the following steps:

    # If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the 
    # four children to Null and stop.
    # If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids
    # as shown in the photo.
    # Recurse for each of the children with the proper sub-grid.


class Node:
    def __init__(self, val, isLeaf, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid):

    def DFS(n, row, col):
        if n == 1:
            return Node(grid[row][col], True)
        
        n //= 2
        topLeft = DFS(n, row, col)
        topRight = DFS(n, row, col + n)
        bottomLeft = DFS(n, row + n, col)
        bottomRight = DFS(n, row + n, col + n)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            
            return Node(topLeft.val, True)

        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
    
    return DFS(len(grid), 0, 0)



grid = [[1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]]

print(construct(grid))