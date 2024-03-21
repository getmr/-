# 顺时针打印矩阵
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
例如，如果输入如下4 X 4矩阵：
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
解题思路：
1. 顺时针打印矩阵的顺序是从左到右，从上到下，从右到左，从下到上
2. 首先遍历第一行，遇到边界转向，并记录已经遍历的行
"""

def print_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    # 定义四个边界
    left, right, top, bottom = 0, cols-1, 0, rows-1
    # 定义方向
    direction = 0
    while True:
        if direction == 0:
            for i in range(left, right+1):
                print(matrix[top][i])
            top += 1
        if direction == 1:
            for i in range(top, bottom+1):
                print(matrix[i][right])
            right -= 1
        if direction == 2:
            for i in range(right, left-1, -1):
                print(matrix[bottom][i])
            bottom -= 1
        if direction == 3:
            for i in range(bottom, top-1, -1):
                print(matrix[i][left])
            left += 1
        if left > right or top > bottom:
            break
        direction = (direction + 1) % 4

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print_matrix(matrix)
    # Expected output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
