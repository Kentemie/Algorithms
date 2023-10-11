# Given a 2D matrix matrix, handle multiple queries of the following types:

    # Update the value of a cell in matrix.
    # Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and 
    # lower right corner (row2, col2).

# Implement the NumMatrix class:

    # NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    # void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
    # int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
    # defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

from math import ceil, log2

class TwoDimensionalSegmentTree:

    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.__two_dimensional_size = 2 ** (ceil(log2(self.rows)) + 1) - 1
        self.__one_dimensional_size = 2 ** (ceil(log2(self.cols)) + 1) - 1
        
        self.two_dimensional_segment_tree = [[]] * self.__two_dimensional_size

        self.__construct(matrix)

    # -- Two dimensional segment tree construction ------------------------- #

    def __construct(self, matrix):
        partial_segment_tree = [[0] * self.__one_dimensional_size for _ in range(self.rows)]

        for i in range(self.rows):
            self.__constuct_one_dimensional_segment_tree(partial_segment_tree[i], matrix[i], 0, self.cols - 1, 0)

        self.__final_constuct(partial_segment_tree, 0, self.rows - 1, 0)

    def __constuct_one_dimensional_segment_tree(self, seg_tree, nums, left, right, tree_idx): 
        if left == right:
            seg_tree[tree_idx] = nums[left]
            return
        
        mid = (left + right) // 2
        self.__constuct_one_dimensional_segment_tree(seg_tree, nums, left, mid, tree_idx * 2 + 1)
        self.__constuct_one_dimensional_segment_tree(seg_tree, nums, mid + 1, right, tree_idx * 2 + 2)

        seg_tree[tree_idx] = seg_tree[tree_idx * 2 + 1] + seg_tree[tree_idx * 2 + 2]

    def __final_constuct(self, part_seg_tree, left, right, tree_idx):
        if left == right:
            self.two_dimensional_segment_tree[tree_idx] = part_seg_tree[left].copy()
            return 
        
        mid = (left + right) // 2
        self.__final_constuct(part_seg_tree, left, mid, tree_idx * 2 + 1)
        self.__final_constuct(part_seg_tree, mid + 1, right, tree_idx * 2 + 2)
        
        self.two_dimensional_segment_tree[tree_idx] = \
            list(map(sum, zip(self.two_dimensional_segment_tree[tree_idx * 2 + 1], \
                              self.two_dimensional_segment_tree[tree_idx * 2 + 2])))

    # -- Getting sum ------------------------------------------------------- #

    def sumRegion(self, row1, col1, row2, col2):
        return self.__query(0, self.rows - 1, row1, col1, row2, col2, 0)
    
    def __query(self, low, high, x1, y1, x2, y2, outer_tree_idx):
        if high < x1 or x2 < low:
            return 0
        
        if x1 <= low and high <= x2:
            return self.__finalQuery(0, self.cols - 1, y1, y2, outer_tree_idx, 0)
        
        mid = (low + high) // 2
        return self.__query(low, mid, x1, y1, x2, y2, outer_tree_idx * 2 + 1) + \
            self.__query(mid + 1, high, x1, y1, x2, y2, outer_tree_idx * 2 + 2)
    
    def __finalQuery(self, left, right, y1, y2, outer_tree_idx, inner_tree_idx):
        if right < y1 or y2 < left:
            return 0
        
        if y1 <= left and right <= y2:
            return self.two_dimensional_segment_tree[outer_tree_idx][inner_tree_idx]
        
        mid = (left + right) // 2
        return self.__finalQuery(left, mid, y1, y2, outer_tree_idx, inner_tree_idx * 2 + 1) + \
            self.__finalQuery(mid + 1, right, y1, y2, outer_tree_idx, inner_tree_idx * 2 + 2)

    # -- Updation ---------------------------------------------------------- #

    def update(self, row, col, val):
        self.__update(0, self.rows - 1, row, col, val, 0)
    
    def __update(self, low, high, x, y, val, outer_tree_idx):
        if low == high:
            self.__finalUpdate(0, self.cols - 1, y, val, outer_tree_idx, 0)
        else:
            mid = (low + high) // 2
            
            if low <= x <= mid:
                self.__update(low, mid, x, y, val, outer_tree_idx * 2 + 1)
            else:
                self.__update(mid + 1, high, x, y, val, outer_tree_idx * 2 + 2)
            
            for i in range(self.__one_dimensional_size):
                self.two_dimensional_segment_tree[outer_tree_idx][i] = \
                    self.two_dimensional_segment_tree[outer_tree_idx * 2 + 1][i] + \
                        self.two_dimensional_segment_tree[outer_tree_idx * 2 + 2][i]
                
    def __finalUpdate(self, left, right, y, val, outer_tree_idx, inner_tree_idx):
        if left == right:
            self.two_dimensional_segment_tree[outer_tree_idx][inner_tree_idx] = val
        else:
            mid = (left + right) // 2

            if left <= y <= mid:
                self.__finalUpdate(left, mid, y, val, outer_tree_idx, inner_tree_idx * 2 + 1)
            else:
                self.__finalUpdate(mid + 1, right, y, val, outer_tree_idx, inner_tree_idx * 2 + 2)

            self.two_dimensional_segment_tree[outer_tree_idx][inner_tree_idx] = \
                self.two_dimensional_segment_tree[outer_tree_idx][inner_tree_idx * 2 + 1] + \
                    self.two_dimensional_segment_tree[outer_tree_idx][inner_tree_idx * 2 + 2]
            

matrix = [[3, 0, 1, 4, 2], 
          [5, 6, 3, 2, 1], 
          [1, 2, 0, 1, 5], 
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]

TDST = TwoDimensionalSegmentTree(matrix)
print(TDST.sumRegion(2, 1, 4, 3))
TDST.update(3, 2, 2)
print(TDST.sumRegion(2, 1, 4, 3))