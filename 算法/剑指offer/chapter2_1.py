# 数组中的重复数字
"""
题目：找出数组中重复的数字
在一个长度为n的数组里的所有数字都在0~n-1的范囿内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
"""
# 方法一：排序
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
def duplicate1(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]
    return -1

# 方法二：哈希表
# 时间复杂度：O(n)
# 空间复杂度：O(n)
def duplicate2(nums):
    hash_map = {}
    for num in nums:
        if num in hash_map:
            return num
        hash_map[num] = 1
    return -1

# 方法三：原地置换
# 时间复杂度：O(n)
# 空间复杂度：O(1)
def duplicate3(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1

# 方法四：二分查找
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
def duplicate4(nums):
    start = 1
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for num in nums:
            if start <= num <= mid:
                count += 1
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


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate1(nums))
    print(duplicate2(nums))
    print(duplicate3(nums))
    print(duplicate4(nums))