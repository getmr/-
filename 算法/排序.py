# 快排

def sort_quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
    return sort_quick(left) + middle + sort_quick(right)


# 在同一个数组生操作实现快排
def sort_quick2(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        sort_quick2(arr, left, pi-1)
        sort_quick2(arr, pi+1, right)


def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print(sort_quick(arr) == [5, 6, 7, 11, 12, 13])
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])
    arr = [12, 11, 13, 5, 6, 7]
    sort_quick2(arr, 0, len(arr)-1)
    print(arr == [5, 6, 7, 11, 12, 13])