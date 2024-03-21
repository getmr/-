"""
题目二：不修改数组找出重复的数字
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的数组。
例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。
"""

# 二分法
# 解题思路：
# 1. 二分法的思路是把1~n的数字从中间的数字m分为两部分，前面一半为1~m，后面一半为m+1~n。
# 2. 如果1~m的数字的数目超过m，那么这一半的区间里一定包含重复的数字；否则，另一半m+1~n的区间里一定包含重复的数字。
# 3. 继续把包含重复数字的区间一分为二，直到找到一个重复的数字。

def count_range(nums, start, end):
    count = 0
    for num in nums:
        if start <= num <= end:
            count += 1
    return count

def duplicate(nums):
    if not nums:
        return -1
    start = 1
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        count = count_range(nums, start, mid)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > mid - start + 1:
            end = mid
        else:
            start = mid + 1
    return -1