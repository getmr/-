class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]


class Solution2:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        temp = n // 3

        if n - temp * 3 == 1:
            temp -= 1
        
        x = n - temp * 3
        return (3 **temp) * x



if __name__ == "__main__":
    print(Solution().cuttingRope(8))
    print(Solution2().cuttingRope(8))

    print(Solution().cuttingRope(16))
    print(Solution2().cuttingRope(16))
