# 斐波那契数列


# 普通方法， 效率最高
def fibonacci(n):
    if n in (0, 1):
        return n
    a = 0
    b = 1
    result = 0
    for _ in range(2, n+1):
        result = a + b
        a = b
        b = result
    return result


# 递归方法
def fibonacci2(n):
    if n in (0, 1):
        return n
    return fibonacci2(n-1) + fibonacci2(n -2)

def fibonacci3(n, memo={}):
    if n in (0, 1):
        return n
    if n not in memo:
        memo[n] = fibonacci3(n-1, memo) + fibonacci3(n-2, memo)
    return memo[n]


# 动态规划方法
def fibonacci4(n):
    if n in (0, 1):
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]



if __name__ == "__main__":
    print(fibonacci(3))
    print(fibonacci2(3))

    print(fibonacci(50))
    print(fibonacci3(50))
