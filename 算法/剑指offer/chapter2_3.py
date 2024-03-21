from typing import List

# 二维数组中的查找
"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样
的一个二维数组和一个整数，判断数组中是否含有该整数。

1  2  8  9
2  4  9  12
4  7  10 13
6  8  11 15
"""

# 方法一：暴力法
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
def find1(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False


# 方法二：从左下角或者右上角开始查找    
# 时间复杂度：O(n)
# 空间复杂度：O(1)
def find2(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    row = len(matrix)
    col = len(matrix[0])
    i = row - 1
    j = 0
    while i >= 0 and j < col:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return False

if __name__ == "__main__":
    matrix = [[1, 2, 8, 9],
              [2, 4, 9, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15]]
    target = 7
    print(find1(matrix, target))
    print(find2(matrix, target))