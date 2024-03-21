"""
题目描述：输入n个整数，找出其中最小的k个数。例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4。
"""

# 方法一：快排思想

def partition(arr, start, end):
    i, j = start, end
    while i < j:
        while i < j and arr[j] > arr[start]:
            j -= 1
        while i < j and arr[i] <= arr[start]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[start] = arr[start], arr[i]
    return i


def get_least_numbers(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []
    start, end = 0, len(arr) - 1
    index = partition(arr, start, end)
    while index != k - 1:
        if index > k - 1:
            end = index - 1
            index = partition(arr, start, end)
        else:
            start = index + 1
            index = partition(arr, start, end)
    return arr[:k]