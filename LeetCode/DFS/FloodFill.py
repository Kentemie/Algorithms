# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel
# image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the
# same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and 
# so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

def floodFill(image, sr, sc, color):
    row, col = len(image), len(image[0])
    oldColor = image[sr][sc]
    if oldColor == color: 
        return image
    def DFS(r, c):
        if image[r][c] == oldColor:
            image[r][c] = color
            if r >= 1:
                DFS(r - 1, c)
            if r + 1 < row:
                DFS(r + 1, c)
            if c >= 1:
                DFS(r, c - 1)
            if c + 1 < col:
                DFS(r, c + 1)
    DFS(sr, sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))