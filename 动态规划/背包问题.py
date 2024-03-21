"""
背包问题
有一个背包，容量为4磅，现有如下物品
物品	重量	价格
吉他	1	1500
音响	4	3000
笔记本	3	2000
请问如何让背包装入最大价值的物品？
"""

# 方法一：动态规划
# 思路
# 1. 用一个二维数组 dp 存储物品的最大价值
# 2. dp[i][j] 表示前 i 个物品，背包容量为 c 时的最大价值
# 3. 状态转移方程：
#    - 若第 i 个物品的重量大于背包容量 c，则不选物品 i, dp[i][c] = dp[i-1][c]
#    - 若第 i 个物品的重量小于等于背包容量 c，则选和不选物品 i 这两种方案的较大值, 不选时，dp[i][c] = dp[i-1][c]，选时，dp[i][c] = dp[i-1][c-wgt[i-1]] + val[i-1]，
#   其中 wgt[i-1] 表示第 i 个物品的重量，val[i-1] 表示第 i 个物品的价值，dp[i-1][c-wgt[i-1]] 表示前 i-1 个物品，背包容量为 c-wgt[i-1] 时的最大价值
# dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt[i]] + val[i])

# 4. 最终返回 dp[n][cap] 即可
def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[i][c] = dp[i - 1][c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


if __name__ == '__main__':
    wgt = [1, 4, 3]
    val = [1500, 3000, 2000]
    cap = 4
    print(knapsack_dp(wgt, val, cap))  # 3500
    wgt = [1, 2, 3]
    val = [6, 10, 12]
    cap = 5
    print(knapsack_dp(wgt, val, cap))  # 22
    wgt = [1, 3, 4]
    val = [15, 20, 30]
    cap = 4
    print(knapsack_dp(wgt, val, cap))  # 35
    wgt = [1, 2, 3]
    val = [10, 15, 40]
    cap = 6
    print(knapsack_dp(wgt, val, cap))  # 65
    wgt = [1, 3, 4]
    val = [15, 20, 30]
    cap = 7
    print(knapsack_dp(wgt, val, cap))  # 50
    # 四个物品，背包容量为 8
    wgt = [2, 3, 4, 5]
    val = [3, 4, 5, 6]
    cap = 8
    print(knapsack_dp(wgt, val, cap))  # 10