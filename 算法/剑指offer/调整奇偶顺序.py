"""
调整数组顺序使奇数位于偶数前面
题目描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
"""     

# 交换方式
def re_order(arr):
    length = len(arr)
    left = 0
    right = length - 1
    while left < right:
        while left < right and arr[left] % 2 != 0:
            left += 1
        while left < right and arr[right] % 2 == 0:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

# 拼接方式
def re_order2(arr):
    left = []
    right = []
    for i in arr:
        if i % 2 == 0:
            right.append(i)
        else:
            left.append(i)
    return left + right
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    re_order(arr)
    print(arr) # [1, 7, 3, 5, 4, 6, 2]
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    re_order(arr)
    print(arr) # [1, 7, 3, 5, 8, 6, 4, 2]
    arr = [1, 3, 5, 7]
    re_order(arr)
    print(arr) # [1, 3, 5, 7]
    arr = [2, 4, 6, 8]
    re_order(arr)
    print(arr) # [2, 4, 6, 8]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    re_order(arr)
    print(arr) # [1, 9, 3, 7, 5, 6, 4, 8, 2]
    arr = [1, 3, 5, 7, 9]
    re_order(arr)
    print(arr) # [1, 3, 5, 7, 9]
    arr = [2, 4, 6, 8, 10]
    re_order(arr)
    print(arr) # [2, 4, 6, 8, 10]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    re_order(arr)
    print(arr) # [1, 9, 3, 7, 5, 6, 4, 8, 10, 2]