"""
完全背包问题
有N种物品和一个容量为V的背包。第i种物品有无限件可用，价值为vi，体积为wi。
求解将哪些物品装入背包可使这些物品的总体积不超过背包容量，且总价值最大。
例如：有3种物品，背包容量为50，每种物品的价值和体积如下：
编号  重量   价值
1      10     50
2      20     120
3      30     150
4      40     210
5      50     240

请问如何让背包装入最大价值的物品？
"""
def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划"""
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
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]

if __name__ == '__main__':
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    cap = 50
    print(unbounded_knapsack_dp(wgt, val, cap))  # 240
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 8
    print(unbounded_knapsack_dp(wgt, val, cap))  # 22
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 9
    print(unbounded_knapsack_dp(wgt, val, cap))  # 25
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 10
    print(unbounded_knapsack_dp(wgt, val, cap))  # 30
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 11
    print(unbounded_knapsack_dp(wgt, val, cap))  # 35
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 12
    print(unbounded_knapsack_dp(wgt, val, cap))  # 40
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 13
    print(unbounded_knapsack_dp(wgt, val, cap))  # 45
    wgt = [1, 2, 3, 4, 5]
    val = [1, 5, 8, 9, 10]
    cap = 14
    print(unbounded_knapsack_dp(wgt, val, cap))  # 50
    wgt = [1, 2, 3, 4, 5]