# 二分查找

# 1. 递归法
def binary_search(arr, left, right, num):
    """
    使用递归方式
    """
    mid = (left + right) // 2
    while left <= right:
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid -1
            return binary_search(arr, left, right, num)
        else:
            left = mid +1
            return binary_search(arr, left, right, num)
    return None


# 2. 不是用递归
def binary_search2(arr, num):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid -1
        else:
            left = mid +1
    return None

if __name__ == "__main__":
    arr =  [2, 3, 4, 10, 40, 50, 55, 70]
    print(binary_search(arr, 0, len(arr)-1, 2) == 0)
    print(binary_search(arr, 0, len(arr)-1, 3) == 1)

    print(binary_search2(arr, 2) == 0)
    print(binary_search2(arr, 3) == 1)
