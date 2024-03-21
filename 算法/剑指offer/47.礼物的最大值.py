"""
礼物的最大值
题目：在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物。
例如，对于如下棋盘
1    10   3   8
12   2    9   6
5    7    4   11
3    7    16  5
"""

# 方法一：动态规划
def get_max_value(arr):
    if not arr:
        return 0
    rows, cols = len(arr), len(arr[0])
    max_values = [[0] * cols for _ in range(rows)]
    # 首行
    for i in range(cols):
        max_values[0][i] = max_values[0][i - 1] + arr[0][i]
    # 首列
    for i in range(1, rows):
        max_values[i][0] = max_values[i - 1][0] + arr[i][0]
    # 状态转移： 其余行与列
    for i in range(1, rows):
        for j in range(1, cols):
            max_values[i][j] = max(max_values[i - 1][j], max_values[i][j - 1]) + arr[i][j]
    return max_values[-1][-1]