"""
给定 种硬币，第 种硬币的面值为 ，目标金额为 ，每种硬币可以重复选取，问能够凑出目标金额的最少硬币数量。
如果无法凑出目标金额，则返回 。示例如图 14-24 所示。
示例 1：
输入：coins = [1, 2, 5], amount = 11
"""

def coin_charge(coins, amount):
    if not coins or amount < 0:
        return -1
    MAX = amount + 1
    n = len(coins)
    dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
    for i in range(1, n+1):
        for a in range(1, amount+1):
            if coins[i-1] > a:
                dp[i][a] = dp[i-1][a]
            else:
                dp[i][a] = min(dp[i-1][a], dp[i][a-coins[i-1]] +1)
    return dp[n][amount] if dp[n][amount] != MAX else -1