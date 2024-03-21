"""
连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O(n)。
"""

def find_greatest_sum_of_sub_array(arr):
    if len(arr) == 0:
        return 0
    cur_sum = 0
    greatest_sum = float('-inf')
    for i in arr:
        if cur_sum <= 0:
            cur_sum = i
        else:
            cur_sum += i
        if cur_sum > greatest_sum:
            greatest_sum = cur_sum
    return greatest_sum


# 动态规划
def find_greatest_sum_of_sub_array2(arr):
    if len(arr) == 0:
        return 0
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(dp)


if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    assert find_greatest_sum_of_sub_array(arr) == 18
    assert find_greatest_sum_of_sub_array2(arr) == 18
    arr = [1, -2, 3, 10, -4, 7, 2, 5]
    print(find_greatest_sum_of_sub_array(arr))  # 23
    arr = [-2, -8, -1, -5, -9]
    print(find_greatest_sum_of_sub_array(arr))  # -1
    arr = [2, 8, 1, 5, 9]
    print(find_greatest_sum_of_sub_array(arr))  # 25
    arr = [2, -8, 1, -5, 9]
    print(find_greatest_sum_of_sub_array(arr))  # 9
    arr = [-2, 8, 1, -5, 9]
    print(find_greatest_sum_of_sub_array(arr))  # 13
    arr = [-2, -8, 1, 5, -9] 
    print(find_greatest_sum_of_sub_array(arr))  # 6
    arr = [2, 8, 1, 5, -9]
    print(find_greatest_sum_of_sub_array(arr))  # 16
    arr = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(find_greatest_sum_of_sub_array(arr))  # 13
    arr = [1, -2, -1, 2, 3, -1, 2]
    print(find_greatest_sum_of_sub_array(arr))  # 7
    arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    print(find_greatest_sum_of_sub_array(arr))  # -1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_greatest_sum_of_sub_array(arr))  # 55