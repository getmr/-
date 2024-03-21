# 斐波那契数列

# 递归
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


# 普通方法
def Fibonacci2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0 
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


# 动态规划
def Fibonacci3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":
    print(Fibonacci(10))
    print(Fibonacci2(10)) 
    print(Fibonacci3(10))