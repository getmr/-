"""
数组中超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如，输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
"""

# 方法一：排序后取中间值
# 时间复杂度O(nlogn)
def more_than_half_num(numbers):
    if not numbers:
        return 0
    numbers.sort()
    mid = len(numbers) // 2
    return numbers[mid] if numbers.count(numbers[mid]) > len(numbers) // 2 else 0


# 方法二：字典法
def more_than_half_num2(numbers):
    if not numbers:
        return 0
    dic = {}
    for i in numbers:
        dic[i] = dic.get(i, 0) + 1
        if dic[i] > len(numbers) // 2:
            return i
    return 0


# 方法三：摩尔投票法
# 这个方法只有在输入的数组中有出现次数超过一半的数字时才会返回正确的结果
def more_than_half_num3(numbers):
    if not numbers:
        return 0
    res = numbers[0]
    count = 1
    for i in numbers[1:]:
        if count == 0:
            res = i
            count = 1
        elif res == i:
            count += 1
        else:
            count -= 1
    return res


# 方法四：partition
# 这个方法只有在输入的数组中有出现次数超过一半的数字时才会返回正确的结果
def more_than_half_num4(numbers):
    if not numbers:
        return 0
    start = 0
    end = len(numbers) - 1
    mid = len(numbers) >> 1
    index = partition(numbers, start, end)
    while index != mid:
        if index > mid:
            end = index - 1
            index = partition(numbers, start, end)
        else:
            start = index + 1
            index = partition(numbers, start, end)
    result = numbers[mid]
    if not check_more_than_half(numbers, result):
        result = 0
    return result

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

def check_more_than_half(numbers, result):
    times = 0
    for i in numbers:
        if i == result:
            times += 1
    return times * 2 > len(numbers)


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(more_than_half_num(numbers))
    print(more_than_half_num2(numbers))
    print(more_than_half_num3(numbers))
    print(more_than_half_num4(numbers))