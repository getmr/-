def pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    cnt = 1
    for i in range(1, n+1):
        cnt *= x
    return cnt

if __name__ == "__main__":
    print(pow(2.00000, 10))