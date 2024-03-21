"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
"""
def find_min(nums):
    left, right = 0, len(nums) -1
    while left < right:
        mid = (left + right) //2
        if nums[mid] > nums[right]:
            left = mid +1
        if nums[mid] < nums[right]:
            right = mid
        else:
            right -=1
    return nums[right]


if __name__ == "__main__":
    print(find_min([3,4,5,1,2]))
    print(find_min([2,2,2,0,1]))