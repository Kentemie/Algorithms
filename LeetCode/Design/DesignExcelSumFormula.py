# Design the basic function of Excel and implement the function of the sum formula.

# Implement the Excel class:

    # Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer
    # matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width].
    # All the values should be zero initially.
    # void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
    # int get(int row, char column) Returns the value at mat[row][column].
    # int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by 
    # numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value
    # or another sum formula. numbers[i] could be on the format:
        # "ColRow" that represents a single cell.
            # For example, "F7" represents the cell mat[7]['F'].
        # "ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent 
        # the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
            # For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.

# Note: You could assume that there will not be any circular sum reference.

    # For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").

class Excel:
    
    def __init__(self, height, width):
        self.matrix = [[{ "value": 0, "sum": None } for _ in range(ord(width) - 64)] for _ in range(height)]
    
    def set(self, row, column, val):
        self.matrix[row - 1][ord(column) - 65] = { "value": val, "sum": None }

    def get(self, row, column):
        cell = self.matrix[row - 1][ord(column) - 65]
        if not cell["sum"]:
            return cell["value"]
        _sum = 0
        for pos in cell["sum"]:
            _sum += self.get(*pos) * cell["sum"][pos]
        return _sum
    
    def sum(self, row, column, numbers):
        self.matrix[row - 1][ord(column) - 65]["sum"] = self.parse(numbers)
        return self.get(row, column)

    def parse(self, numbers):
        counter = {}
        for s in numbers:
            s, e = s.split(":")[0], s.split(":")[1] if ":" in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    col = chr(j + 64)
                    counter[(i, col)] = counter.get((i, col), 0) + 1

        return counter
    
excel = Excel(3,"D")
excel.set(1, "A", 2)
print(excel.sum(3, "C", ["A1", "A1:B2"]))
excel.set(2, "B", 2)
print(excel.get(3, "C"))

for row in excel.matrix:
    print(row)